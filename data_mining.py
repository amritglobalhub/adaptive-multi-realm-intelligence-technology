"""
AMRIT AI - Data Mining Pipeline

Extracts and analyzes user patterns for personalization.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
from collections import Counter
import json
import numpy as np
import config
from hidden_storage import HiddenStorageManager


class DataMiningPipeline:
    """Mines user data for personalization insights"""
    
    def __init__(self, storage_manager: HiddenStorageManager):
        """
        Initialize data mining pipeline
        
        Args:
            storage_manager: Hidden storage manager
        """
        self.storage = storage_manager
        self.mined_insights = {}
        self._load_insights()
    
    def _load_insights(self):
        """Load previously mined insights"""
        try:
            data = self.storage.retrieve_data(
                'system_intelligence',
                'mined_insights'
            )
            if data:
                self.mined_insights = data
        except:
            pass
    
    def _save_insights(self):
        """Save mined insights"""
        self.storage.store_data(
            'system_intelligence',
            'mined_insights',
            self.mined_insights
        )
    
    def mine_command_preferences(self, interaction_history: List) -> Dict:
        """
        Mine command preferences from interaction history
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of command preferences
        """
        command_prefs = {
            'most_used': [],
            'preferred_time': {},
            'success_patterns': {},
            'context_associations': {}
        }
        
        commands = []
        command_times = {}
        
        for record in interaction_history:
            if record.type == 'command':
                cmd = record.data.get('command', '')
                if cmd:
                    commands.append(cmd)
                    
                    # Track time of day
                    timestamp = datetime.fromisoformat(record.timestamp)
                    hour = timestamp.hour
                    
                    if cmd not in command_times:
                        command_times[cmd] = []
                    command_times[cmd].append(hour)
        
        # Most used commands
        command_counts = Counter(commands)
        command_prefs['most_used'] = [
            {'command': cmd, 'count': count}
            for cmd, count in command_counts.most_common(10)
        ]
        
        # Preferred time patterns
        for cmd, hours in command_times.items():
            command_prefs['preferred_time'][cmd] = {
                'peak_hour': Counter(hours).most_common(1)[0][0] if hours else None,
                'avg_hour': np.mean(hours) if hours else None
            }
        
        return command_prefs
    
    def mine_response_preferences(self, interaction_history: List) -> Dict:
        """
        Mine response style preferences
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of response preferences
        """
        response_prefs = {
            'preferred_length': 'medium',
            'preferred_style': 'balanced',
            'detail_level': 'moderate',
            'technical_level': 'moderate'
        }
        
        response_lengths = []
        
        for record in interaction_history:
            if 'response' in record.data:
                response = record.data['response']
                if isinstance(response, str):
                    response_lengths.append(len(response.split()))
                
                # Check satisfaction if available
                if 'satisfaction' in record.data:
                    satisfaction = record.data['satisfaction']
                    # Adjust preferences based on satisfaction
                    # (simplified logic)
                    if satisfaction > 0.8:
                        # This response was satisfactory
                        pass
        
        # Analyze preferred length
        if response_lengths:
            avg_length = np.mean(response_lengths)
            if avg_length < 50:
                response_prefs['preferred_length'] = 'brief'
            elif avg_length > 200:
                response_prefs['preferred_length'] = 'detailed'
            else:
                response_prefs['preferred_length'] = 'medium'
        
        return response_prefs
    
    def mine_time_patterns(self, interaction_history: List) -> Dict:
        """
        Mine temporal usage patterns
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of time patterns
        """
        time_patterns = {
            'active_hours': [],
            'active_days': [],
            'peak_times': {},
            'session_durations': []
        }
        
        hours = []
        days = []
        sessions = {}
        
        for record in interaction_history:
            timestamp = datetime.fromisoformat(record.timestamp)
            hours.append(timestamp.hour)
            days.append(timestamp.strftime('%A'))
            
            # Group into sessions (within 30 min = same session)
            session_key = timestamp.strftime('%Y-%m-%d-%H')
            if session_key not in sessions:
                sessions[session_key] = []
            sessions[session_key].append(timestamp)
        
        # Most active hours
        hour_counts = Counter(hours)
        time_patterns['active_hours'] = [
            {'hour': hour, 'count': count}
            for hour, count in hour_counts.most_common(5)
        ]
        
        # Most active days
        day_counts = Counter(days)
        time_patterns['active_days'] = [
            {'day': day, 'count': count}
            for day, count in day_counts.most_common()
        ]
        
        # Calculate session durations
        for session_times in sessions.values():
            if len(session_times) > 1:
                duration = (max(session_times) - min(session_times)).seconds
                time_patterns['session_durations'].append(duration)
        
        return time_patterns
    
    def mine_context_understanding(self, interaction_history: List) -> Dict:
        """
        Mine context and domain understanding
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of context insights
        """
        context_insights = {
            'topics_of_interest': [],
            'knowledge_domains': [],
            'common_contexts': []
        }
        
        topics = []
        contexts = []
        
        for record in interaction_history:
            # Extract topics from queries and commands
            if 'topic' in record.data:
                topics.append(record.data['topic'])
            
            if 'context' in record.data:
                ctx = record.data['context']
                if isinstance(ctx, dict):
                    contexts.append(json.dumps(ctx))
        
        # Most common topics
        if topics:
            topic_counts = Counter(topics)
            context_insights['topics_of_interest'] = [
                {'topic': topic, 'frequency': count}
                for topic, count in topic_counts.most_common(10)
            ]
        
        return context_insights
    
    def mine_communication_style(self, linguistic_patterns: Dict) -> Dict:
        """
        Mine communication style from linguistic patterns
        
        Args:
            linguistic_patterns: Dictionary of linguistic patterns
            
        Returns:
            Dictionary of communication style insights
        """
        style = {
            'formality_level': 'neutral',
            'verbosity': 'moderate',
            'technical_vocabulary': False,
            'common_expressions': [],
            'sentence_complexity': 'medium'
        }
        
        # Analyze word frequency for technical terms
        word_freq = linguistic_patterns.get('word_frequency', {})
        if word_freq:
            # Check for technical terms (simplified)
            technical_terms = ['algorithm', 'system', 'data', 'model', 'function']
            tech_count = sum(word_freq.get(term, 0) for term in technical_terms)
            style['technical_vocabulary'] = tech_count > 10
        
        # Analyze sentence lengths
        sentence_lengths = linguistic_patterns.get('sentence_lengths', [])
        if sentence_lengths:
            avg_length = np.mean(sentence_lengths)
            if avg_length < 8:
                style['sentence_complexity'] = 'simple'
            elif avg_length > 20:
                style['sentence_complexity'] = 'complex'
            else:
                style['sentence_complexity'] = 'medium'
        
        # Get common expressions
        common_phrases = linguistic_patterns.get('common_phrases', {})
        if common_phrases:
            sorted_phrases = sorted(
                common_phrases.items(),
                key=lambda x: x[1],
                reverse=True
            )
            style['common_expressions'] = [p for p, _ in sorted_phrases[:10]]
        
        return style
    
    def mine_decision_patterns(self, interaction_history: List) -> Dict:
        """
        Mine decision-making patterns
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of decision patterns
        """
        decision_patterns = {
            'decision_speed': 'moderate',
            'preference_consistency': 0.0,
            'choice_patterns': {}
        }
        
        decisions = []
        decision_times = []
        
        for record in interaction_history:
            if record.type == 'decision' or 'choice' in record.data:
                decisions.append(record.data.get('choice', ''))
                
                # Track decision time if available
                if 'decision_time' in record.data:
                    decision_times.append(record.data['decision_time'])
        
        # Analyze decision speed
        if decision_times:
            avg_time = np.mean(decision_times)
            if avg_time < 5:  # seconds
                decision_patterns['decision_speed'] = 'fast'
            elif avg_time > 30:
                decision_patterns['decision_speed'] = 'deliberate'
            else:
                decision_patterns['decision_speed'] = 'moderate'
        
        # Analyze consistency
        if len(decisions) > 10:
            unique_decisions = len(set(decisions))
            decision_patterns['preference_consistency'] = 1.0 - (unique_decisions / len(decisions))
        
        return decision_patterns
    
    def mine_emotional_undertones(self, interaction_history: List) -> Dict:
        """
        Mine emotional patterns from interactions
        
        Args:
            interaction_history: List of interaction records
            
        Returns:
            Dictionary of emotional patterns
        """
        emotional_patterns = {
            'overall_sentiment': 'neutral',
            'emotion_distribution': {},
            'stress_indicators': []
        }
        
        sentiments = []
        
        for record in interaction_history:
            # Check for sentiment data
            if 'sentiment' in record.data:
                sentiments.append(record.data['sentiment'])
            
            # Check for emotional indicators in text
            text = record.data.get('text', '').lower()
            
            # Simple keyword-based emotion detection
            if any(word in text for word in ['urgent', 'immediately', 'asap']):
                emotional_patterns['stress_indicators'].append(record.timestamp)
        
        # Calculate overall sentiment
        if sentiments:
            avg_sentiment = np.mean(sentiments)
            if avg_sentiment < -0.3:
                emotional_patterns['overall_sentiment'] = 'negative'
            elif avg_sentiment > 0.3:
                emotional_patterns['overall_sentiment'] = 'positive'
            else:
                emotional_patterns['overall_sentiment'] = 'neutral'
        
        return emotional_patterns
    
    def run_full_analysis(self, interaction_history: List, 
                         linguistic_patterns: Dict) -> Dict:
        """
        Run complete data mining analysis
        
        Args:
            interaction_history: List of interaction records
            linguistic_patterns: Dictionary of linguistic patterns
            
        Returns:
            Complete insights dictionary
        """
        insights = {
            'command_preferences': self.mine_command_preferences(interaction_history),
            'response_preferences': self.mine_response_preferences(interaction_history),
            'time_patterns': self.mine_time_patterns(interaction_history),
            'context_understanding': self.mine_context_understanding(interaction_history),
            'communication_style': self.mine_communication_style(linguistic_patterns),
            'decision_patterns': self.mine_decision_patterns(interaction_history),
            'emotional_patterns': self.mine_emotional_undertones(interaction_history),
            'analyzed_at': datetime.now().isoformat(),
            'sample_size': len(interaction_history)
        }
        
        self.mined_insights = insights
        self._save_insights()
        
        return insights
    
    def get_insights(self) -> Dict:
        """Get current mined insights"""
        return self.mined_insights
    
    def get_personalization_profile(self) -> Dict:
        """
        Get comprehensive personalization profile
        
        Returns:
            Dictionary suitable for personalization
        """
        if not self.mined_insights:
            return {}
        
        profile = {
            'preferences': {
                'command_style': self.mined_insights.get('command_preferences', {}).get('most_used', [])[:3],
                'response_style': self.mined_insights.get('response_preferences', {}),
                'communication': self.mined_insights.get('communication_style', {})
            },
            'patterns': {
                'time': self.mined_insights.get('time_patterns', {}),
                'decision': self.mined_insights.get('decision_patterns', {})
            },
            'context': self.mined_insights.get('context_understanding', {}),
            'emotional_profile': self.mined_insights.get('emotional_patterns', {})
        }
        
        return profile
