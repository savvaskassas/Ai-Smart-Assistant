from datetime import datetime, timedelta
from typing import List, Dict, Any

def suggest_daily_plan(events: List[Dict[str, Any]], priorities: List[str] = None) -> Dict[str, Any]:
    """
    Generate an optimized daily plan based on calendar events.
    
    Args:
        events: List of calendar events with start/end times
        priorities: Optional list of priority keywords
    
    Returns:
        Dictionary containing structured daily plan with recommendations
    """
    if not events:
        return {
            "status": "success",
            "plan": [
                {
                    "time": "09:00",
                    "activity": "Start your day with planning",
                    "type": "suggestion",
                    "duration": 30
                },
                {
                    "time": "09:30",
                    "activity": "Focus time for deep work",
                    "type": "suggestion",
                    "duration": 120
                },
                {
                    "time": "12:00",
                    "activity": "Lunch break",
                    "type": "suggestion",
                    "duration": 60
                },
                {
                    "time": "14:00",
                    "activity": "Productive afternoon session",
                    "type": "suggestion",
                    "duration": 120
                },
                {
                    "time": "17:00",
                    "activity": "Review and plan for tomorrow",
                    "type": "suggestion",
                    "duration": 30
                }
            ],
            "summary": "No scheduled events. Focus on personal tasks and deep work.",
            "free_time_blocks": [
                {"start": "09:00", "end": "17:30", "duration_minutes": 510}
            ]
        }
    
    # Sort events by start time
    sorted_events = sorted(events, key=lambda e: e.get('start', {}).get('dateTime', e.get('start', {}).get('date', '')))
    
    plan = []
    free_blocks = []
    current_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    end_of_day = datetime.now().replace(hour=18, minute=0, second=0, microsecond=0)
    
    for event in sorted_events:
        start_str = event.get('start', {}).get('dateTime', event.get('start', {}).get('date'))
        end_str = event.get('end', {}).get('dateTime', event.get('end', {}).get('date'))
        
        if not start_str:
            continue
            
        try:
            event_start = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
            event_end = datetime.fromisoformat(end_str.replace('Z', '+00:00')) if end_str else event_start + timedelta(hours=1)
            
            # Check for free time before this event
            if current_time < event_start:
                free_duration = int((event_start - current_time).total_seconds() / 60)
                if free_duration >= 30:
                    free_blocks.append({
                        "start": current_time.strftime("%H:%M"),
                        "end": event_start.strftime("%H:%M"),
                        "duration_minutes": free_duration
                    })
                    
                    # Add suggestion for free time
                    if free_duration >= 90:
                        plan.append({
                            "time": current_time.strftime("%H:%M"),
                            "activity": "Deep work session - Focus on high priority tasks",
                            "type": "suggestion",
                            "duration": min(free_duration - 30, 120)
                        })
                    elif free_duration >= 45:
                        plan.append({
                            "time": current_time.strftime("%H:%M"),
                            "activity": "Quick task completion - Handle urgent items",
                            "type": "suggestion",
                            "duration": free_duration - 15
                        })
            
            # Add the actual event
            duration = int((event_end - event_start).total_seconds() / 60)
            plan.append({
                "time": event_start.strftime("%H:%M"),
                "activity": event.get('summary', 'Scheduled event'),
                "type": "event",
                "duration": duration,
                "location": event.get('location', 'Not specified')
            })
            
            current_time = event_end
            
        except Exception as e:
            continue
    
    # Check for free time at the end of the day
    if current_time < end_of_day:
        free_duration = int((end_of_day - current_time).total_seconds() / 60)
        if free_duration >= 30:
            free_blocks.append({
                "start": current_time.strftime("%H:%M"),
                "end": end_of_day.strftime("%H:%M"),
                "duration_minutes": free_duration
            })
            plan.append({
                "time": current_time.strftime("%H:%M"),
                "activity": "End of day review and planning",
                "type": "suggestion",
                "duration": 30
            })
    
    total_free_minutes = sum(b['duration_minutes'] for b in free_blocks)
    total_scheduled_minutes = sum(p['duration'] for p in plan if p['type'] == 'event')
    
    return {
        "status": "success",
        "plan": plan,
        "summary": f"{len([p for p in plan if p['type'] == 'event'])} scheduled events, {len(free_blocks)} free time blocks",
        "free_time_blocks": free_blocks,
        "statistics": {
            "total_free_minutes": total_free_minutes,
            "total_scheduled_minutes": total_scheduled_minutes,
            "productivity_score": min(100, int((total_scheduled_minutes / 480) * 100)) if total_scheduled_minutes > 0 else 0
        }
    }