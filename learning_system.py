"""
AMRIT AI Learning and Adaptation System
Continuously learns from user interactions and adapts behavior
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import amrit_config as config
from secure_storage import secure_storage


class LearningSystem:
    """
    Adaptive learning system for AMRIT AI
    Learns patterns, preferences, and anticipates user needs
    """
    
    def __init__(self):
        self.learning_stats = {
            'total_interactions': 0,
            'patterns_learned': 0,
            'preferences_captured': 0,
            'suggestions_made': 0,
            'accuracy_rate': 0.0
        }
        self._load_learning_stats()
    
    def _load_learning_stats(self):
        """Load learning statistics from storage"""
        stats = secure_storage.load_preference('learning_stats')
        if stats:
            self.learning_stats.update(stats)
    
    def _save_learning_stats(self):
        """Save learning statistics to storage"""
        secure_storage.save_preference('learning_stats', self.learning_stats)
    
    def record_interaction(self, interaction_type: str, interaction_data: Dict[str, Any]):
        """
        Record user interaction for learning
        
        Args:
            interaction_type: Type of interaction (command, feedback, etc.)
            interaction_data: Data about the interaction
        """
        interaction_record = {
            'type': interaction_type,
            'data': interaction_data,
            'timestamp': datetime.now().isoformat()
        }
        
        secure_storage.save_learned_pattern('interactions', interaction_record)
        
        self.learning_stats['total_interactions'] += 1
        self._save_learning_stats()
    
    def analyze_patterns(self) -> Dict[str, Any]:
        """
        Analyze learned patterns to extract insights
        
        Returns:
            Analysis results with identified patterns
        """
        # Load all interaction patterns
        interactions = secure_storage.load_learned_patterns('interactions')
        code_patterns = secure_storage.load_learned_patterns('code_generation')
        design_patterns = secure_storage.load_learned_patterns('design_generation')
        voice_patterns = secure_storage.load_learned_patterns('voice_commands')
        
        analysis = {
            'total_interactions': len(interactions),
            'patterns_identified': []
        }
        
        # Analyze coding patterns
        if code_patterns:
            languages = {}
            project_types = {}
            
            for pattern in code_patterns:
                lang = pattern.get('language', 'Unknown')
                proj_type = pattern.get('project_type', 'Unknown')
                
                languages[lang] = languages.get(lang, 0) + 1
                project_types[proj_type] = project_types.get(proj_type, 0) + 1
            
            analysis['patterns_identified'].append({
                'category': 'coding_preferences',
                'most_used_language': max(languages.items(), key=lambda x: x[1])[0] if languages else None,
                'most_built_project_type': max(project_types.items(), key=lambda x: x[1])[0] if project_types else None,
                'language_distribution': languages,
                'project_type_distribution': project_types
            })
        
        # Analyze design patterns
        if design_patterns:
            design_types = {}
            
            for pattern in design_patterns:
                dtype = pattern.get('design_type', 'Unknown')
                design_types[dtype] = design_types.get(dtype, 0) + 1
            
            analysis['patterns_identified'].append({
                'category': 'design_preferences',
                'most_requested_design': max(design_types.items(), key=lambda x: x[1])[0] if design_types else None,
                'design_type_distribution': design_types
            })
        
        # Analyze time patterns
        if interactions:
            hours = {}
            for interaction in interactions:
                timestamp = interaction.get('timestamp', '')
                if timestamp:
                    try:
                        dt = datetime.fromisoformat(timestamp)
                        hour = dt.hour
                        hours[hour] = hours.get(hour, 0) + 1
                    except:
                        pass
            
            if hours:
                peak_hour = max(hours.items(), key=lambda x: x[1])[0]
                analysis['patterns_identified'].append({
                    'category': 'usage_patterns',
                    'peak_usage_hour': peak_hour,
                    'usage_distribution': hours
                })
        
        self.learning_stats['patterns_learned'] = len(analysis['patterns_identified'])
        self._save_learning_stats()
        
        return analysis
    
    def make_suggestion(self, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Make intelligent suggestions based on learned patterns
        
        Args:
            context: Optional context for the suggestion
        
        Returns:
            Suggestion with reasoning
        """
        # Analyze current patterns
        patterns = self.analyze_patterns()
        
        suggestions = []
        
        # Suggest based on coding patterns
        for pattern in patterns.get('patterns_identified', []):
            if pattern['category'] == 'coding_preferences':
                if pattern.get('most_used_language'):
                    suggestions.append({
                        'type': 'code_generation',
                        'suggestion': f"Create a new {pattern['most_used_language']} project",
                        'reason': f"You frequently work with {pattern['most_used_language']}",
                        'confidence': 0.85
                    })
                
                if pattern.get('most_built_project_type'):
                    suggestions.append({
                        'type': 'project_template',
                        'suggestion': f"Try building a {pattern['most_built_project_type']}",
                        'reason': f"Based on your preference for {pattern['most_built_project_type']} projects",
                        'confidence': 0.80
                    })
            
            elif pattern['category'] == 'design_preferences':
                if pattern.get('most_requested_design'):
                    suggestions.append({
                        'type': 'design_generation',
                        'suggestion': f"Generate a new {pattern['most_requested_design']}",
                        'reason': f"You often create {pattern['most_requested_design']} designs",
                        'confidence': 0.75
                    })
            
            elif pattern['category'] == 'usage_patterns':
                peak_hour = pattern.get('peak_usage_hour')
                current_hour = datetime.now().hour
                
                if peak_hour and abs(current_hour - peak_hour) <= 1:
                    suggestions.append({
                        'type': 'productivity',
                        'suggestion': "This is your peak productivity time",
                        'reason': f"You're most active around {peak_hour}:00",
                        'confidence': 0.70
                    })
        
        self.learning_stats['suggestions_made'] += len(suggestions)
        self._save_learning_stats()
        
        return {
            'suggestions': suggestions,
            'total_suggestions': len(suggestions),
            'context': context
        }
    
    def anticipate_need(self, recent_activity: List[str]) -> Dict[str, Any]:
        """
        Anticipate user needs based on recent activity
        
        Args:
            recent_activity: List of recent activities/commands
        
        Returns:
            Anticipated needs and recommendations
        """
        anticipations = []
        
        # Check for sequential patterns
        if len(recent_activity) >= 2:
            last_activities = recent_activity[-2:]
            
            # If user created code, suggest design
            if any('code' in act.lower() for act in last_activities):
                anticipations.append({
                    'need': 'UI/UX Design',
                    'reason': 'You just generated code. You might need a design for the UI.',
                    'action': 'generate_design',
                    'confidence': 0.75
                })
            
            # If user created design, suggest code implementation
            if any('design' in act.lower() for act in last_activities):
                anticipations.append({
                    'need': 'Code Implementation',
                    'reason': 'You created a design. You might want to implement it.',
                    'action': 'generate_code',
                    'confidence': 0.80
                })
            
            # If user has been active, suggest optimization
            if len(recent_activity) >= 5:
                anticipations.append({
                    'need': 'Project Optimization',
                    'reason': 'You\'ve been working actively. Consider optimizing your projects.',
                    'action': 'optimize_projects',
                    'confidence': 0.65
                })
        
        return {
            'anticipations': anticipations,
            'total_anticipations': len(anticipations)
        }
    
    def learn_from_feedback(self, action: str, feedback: str, rating: Optional[int] = None):
        """
        Learn from user feedback on actions
        
        Args:
            action: Action that was taken
            feedback: User feedback
            rating: Optional rating (1-5)
        """
        feedback_data = {
            'action': action,
            'feedback': feedback,
            'rating': rating
        }
        
        secure_storage.save_learned_pattern('feedback', feedback_data)
        
        # Update accuracy rate if rating provided
        if rating:
            feedbacks = secure_storage.load_learned_patterns('feedback')
            ratings = [f.get('rating', 0) for f in feedbacks if f.get('rating')]
            
            if ratings:
                avg_rating = sum(ratings) / len(ratings)
                self.learning_stats['accuracy_rate'] = (avg_rating / 5.0) * 100
                self._save_learning_stats()
    
    def get_learning_progress(self) -> Dict[str, Any]:
        """Get learning system progress and statistics"""
        
        # Calculate learning phase based on interactions
        total = self.learning_stats['total_interactions']
        
        if total < 50:
            phase = 'Recognition'
            progress = (total / 50) * 100
        elif total < 200:
            phase = 'Learning'
            progress = ((total - 50) / 150) * 100
        elif total < 500:
            phase = 'Adaptation'
            progress = ((total - 200) / 300) * 100
        else:
            phase = 'Mastery'
            progress = 100
        
        return {
            'current_phase': phase,
            'progress_percentage': min(progress, 100),
            'statistics': self.learning_stats,
            'next_milestone': self._get_next_milestone(total)
        }
    
    def _get_next_milestone(self, total_interactions: int) -> Optional[Dict[str, Any]]:
        """Get next learning milestone"""
        milestones = [
            {'interactions': 50, 'phase': 'Learning', 'message': 'Moving to Learning phase'},
            {'interactions': 200, 'phase': 'Adaptation', 'message': 'Moving to Adaptation phase'},
            {'interactions': 500, 'phase': 'Mastery', 'message': 'Achieving Mastery'}
        ]
        
        for milestone in milestones:
            if total_interactions < milestone['interactions']:
                return {
                    'interactions_needed': milestone['interactions'] - total_interactions,
                    'next_phase': milestone['phase'],
                    'message': milestone['message']
                }
        
        return None
    
    def improve_performance(self) -> Dict[str, Any]:
        """Analyze and suggest performance improvements"""
        
        patterns = self.analyze_patterns()
        
        improvements = []
        
        # Suggest based on usage patterns
        for pattern in patterns.get('patterns_identified', []):
            if pattern['category'] == 'coding_preferences':
                lang = pattern.get('most_used_language')
                if lang:
                    improvements.append({
                        'area': 'Code Generation',
                        'suggestion': f'Optimize {lang} code generation templates',
                        'impact': 'High',
                        'effort': 'Medium'
                    })
        
        return {
            'improvements_identified': len(improvements),
            'improvements': improvements,
            'applied': False  # User must approve
        }


# Global learning system instance
learning_system = LearningSystem()
