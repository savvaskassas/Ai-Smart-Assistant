from datetime import datetime, timedelta
from typing import List, Dict, Any
from collections import defaultdict
import statistics

def analyze_productivity(activity_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze productivity patterns from calendar events and activity data.
    
    Args:
        activity_data: List of events/activities with timestamps and metadata
    
    Returns:
        Dictionary containing detailed productivity analysis and recommendations
    """
    if not activity_data:
        return {
            "status": "no_data",
            "message": "No activity data available for analysis",
            "recommendations": [
                "Start scheduling your activities to track productivity",
                "Add more events to your calendar for better insights",
                "Use email-to-calendar feature to auto-import events"
            ]
        }
    
    # Initialize analysis metrics
    total_events = len(activity_data)
    total_minutes = 0
    event_types = defaultdict(int)
    hourly_distribution = defaultdict(float)
    daily_patterns = defaultdict(list)
    duration_list = []
    
    # Process each event
    for event in activity_data:
        try:
            start_str = event.get('start', {}).get('dateTime', event.get('start', {}).get('date'))
            end_str = event.get('end', {}).get('dateTime', event.get('end', {}).get('date'))
            
            if not start_str or not end_str:
                continue
            
            start_dt = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
            end_dt = datetime.fromisoformat(end_str.replace('Z', '+00:00'))
            
            duration = (end_dt - start_dt).total_seconds() / 60
            total_minutes += duration
            duration_list.append(duration)
            
            # Hour distribution
            hour = start_dt.hour
            hourly_distribution[hour] += duration
            
            # Daily pattern
            day_of_week = start_dt.strftime('%A')
            daily_patterns[day_of_week].append(duration)
            
            # Event type categorization
            summary = event.get('summary', '').lower()
            if any(word in summary for word in ['meeting', 'call', 'sync', 'standup', 'συνάντηση']):
                event_types['meetings'] += 1
            elif any(word in summary for word in ['deadline', 'delivery', 'submit', 'προθεσμία']):
                event_types['deadlines'] += 1
            elif any(word in summary for word in ['break', 'lunch', 'διάλειμμα']):
                event_types['breaks'] += 1
            elif any(word in summary for word in ['focus', 'work', 'development', 'coding', 'εργασία']):
                event_types['focused_work'] += 1
            else:
                event_types['other'] += 1
                
        except Exception as e:
            continue
    
    # Calculate statistics
    avg_duration = statistics.mean(duration_list) if duration_list else 0
    median_duration = statistics.median(duration_list) if duration_list else 0
    
    # Find peak productivity hours
    peak_hours = sorted(hourly_distribution.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Find most productive day
    daily_totals = {day: sum(durations) for day, durations in daily_patterns.items()}
    most_productive_day = max(daily_totals.items(), key=lambda x: x[1])[0] if daily_totals else "N/A"
    
    # Generate recommendations based on analysis
    recommendations = []
    
    if event_types.get('meetings', 0) > total_events * 0.5:
        recommendations.append("⚠️ High meeting load detected (>50%). Consider blocking focus time.")
    
    if avg_duration < 30:
        recommendations.append("💡 Many short events detected. Try batching similar tasks together.")
    
    if event_types.get('breaks', 0) < total_events * 0.1:
        recommendations.append("☕ Schedule more breaks for better productivity and well-being.")
    
    if len(hourly_distribution) < 6:
        recommendations.append("📅 Consider spreading activities across more hours for better time management.")
    
    if event_types.get('focused_work', 0) < total_events * 0.2:
        recommendations.append("🎯 Schedule more dedicated focus time blocks for deep work.")
    
    if not recommendations:
        recommendations.append("✅ Great job! Your schedule looks balanced and productive.")
    
    # Calculate productivity score
    balance_score = min(100, (len(hourly_distribution) / 8) * 100)
    break_score = min(100, (event_types.get('breaks', 0) / max(1, total_events)) * 100 * 10)
    focus_score = min(100, (event_types.get('focused_work', 0) / max(1, total_events)) * 100 * 5)
    
    productivity_score = int((balance_score + break_score + focus_score) / 3)
    
    return {
        "status": "success",
        "total_events": total_events,
        "total_time_minutes": round(total_minutes, 2),
        "total_time_hours": round(total_minutes / 60, 2),
        "average_event_duration": round(avg_duration, 2),
        "median_event_duration": round(median_duration, 2),
        "event_types": dict(event_types),
        "peak_productivity_hours": [f"{hour:02d}:00 ({round(mins/60, 1)}h)" for hour, mins in peak_hours],
        "most_productive_day": most_productive_day,
        "daily_breakdown": {day: round(sum(durations)/60, 2) for day, durations in daily_patterns.items()},
        "productivity_score": productivity_score,
        "recommendations": recommendations,
        "insights": {
            "meeting_percentage": round((event_types.get('meetings', 0) / max(1, total_events)) * 100, 1),
            "focus_time_percentage": round((event_types.get('focused_work', 0) / max(1, total_events)) * 100, 1),
            "break_percentage": round((event_types.get('breaks', 0) / max(1, total_events)) * 100, 1),
            "time_utilization": round((total_minutes / (8 * 60)) * 100, 1) if total_minutes else 0
        }
    }


def get_weekly_trends(weekly_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyze weekly productivity trends.
    
    Args:
        weekly_data: List of daily productivity data for the week
    
    Returns:
        Weekly trends and patterns
    """
    if not weekly_data:
        return {"status": "no_data", "message": "No weekly data available"}
    
    daily_hours = []
    for day_data in weekly_data:
        daily_hours.append(day_data.get('total_time_hours', 0))
    
    avg_daily_hours = statistics.mean(daily_hours) if daily_hours else 0
    trend = "increasing" if len(daily_hours) > 1 and daily_hours[-1] > daily_hours[0] else "stable"
    
    return {
        "average_daily_hours": round(avg_daily_hours, 2),
        "trend": trend,
        "most_productive_days": sorted(enumerate(daily_hours), key=lambda x: x[1], reverse=True)[:3],
        "consistency_score": round((1 - (statistics.stdev(daily_hours) / max(0.1, avg_daily_hours))) * 100, 1) if len(daily_hours) > 1 else 100
    }