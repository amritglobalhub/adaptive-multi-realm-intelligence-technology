"""
AMRIT AI - Self-Learning Engine

Autonomous learning system that learns from interactions without explicit training.
Captures patterns, preferences, and behaviors.
"""

import numpy as np
from typing import Dict, List, Optional, Any
from datetime import datetime
from collections import defaultdict, Counter
import json
import config
from hidden_storage import HiddenStorageManager
from permission_manager import PermissionManager, PermissionType


class InteractionRecord:
    """Records a single interaction with the system"""
    
    def __init__(self, interaction_type: str, data: Dict):
        self.id = f"int_{datetime.now().timestamp()}"
        self.timestamp = datetime.now().isoformat()
        self.type = interaction_type
        self.data = data
        self.learned = False
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'type': self.type,
            'data': self.data,
            'learned': self.learned
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        record = cls(data['type'], data['data'])
        record.id = data['id']
        record.timestamp = data['timestamp']
        record.learned = data.get('learned', False)
        return record


class LearningModel:
    """Base class for learned models"""
    
    def __init__(self, model_type: str):
        self.model_type = model_type
        self.created_at = datetime.now().isoformat()
        self.last_updated = datetime.now().isoformat()
        self.training_samples = 0
        self.accuracy = 0.0
        self.parameters = {}
    
    def to_dict(self) -> Dict:
        return {
            'model_type': self.model_type,
            'created_at': self.created_at,
            'last_updated': self.last_updated,
            'training_samples': self.training_samples,
            'accuracy': self.accuracy,
            'parameters': self.parameters
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        model = cls(data['model_type'])
        model.created_at = data.get('created_at', model.created_at)
        model.last_updated = data.get('last_updated', model.last_updated)
        model.training_samples = data.get('training_samples', 0)
        model.accuracy = data.get('accuracy', 0.0)
        model.parameters = data.get('parameters', {})
        return model


class SelfLearningEngine:
    """Autonomous learning system"""
    
    def __init__(self, storage_manager: HiddenStorageManager,
                 permission_manager: PermissionManager):
        """
        Initialize self-learning engine
        
        Args:
            storage_manager: Hidden storage manager
            permission_manager: Permission manager
        """
        self.storage = storage_manager
        self.permissions = permission_manager
        self.interaction_history = []
        self.learned_patterns = {}
        self.preference_models = {}
        self.behavioral_models = {}
        self.linguistic_patterns = {}
        self.prediction_models = {}
        
        self._load_learning_state()
    
    def _load_learning_state(self):
        """Load learning state from storage"""
        try:
            # Load interaction history
            history_data = self.storage.retrieve_data(
                'learning_logs',
                'interaction_history'
            )
            if history_data:
                self.interaction_history = [
                    InteractionRecord.from_dict(d) for d in history_data
                ]
            
            # Load learned patterns
            patterns_data = self.storage.retrieve_data(
                'learning_logs',
                'learned_patterns'
            )
            if patterns_data:
                self.learned_patterns = patterns_data
            
            # Load preference models
            prefs_data = self.storage.retrieve_data(
                'behavior_profiles',
                'preference_models'
            )
            if prefs_data:
                self.preference_models = prefs_data
            
            # Load linguistic patterns
            ling_data = self.storage.retrieve_data(
                'behavior_profiles',
                'linguistic_patterns'
            )
            if ling_data:
                self.linguistic_patterns = ling_data
            
        except Exception as e:
            print(f"Error loading learning state: {e}")
    
    def _save_learning_state(self):
        """Save learning state to storage"""
        try:
            # Save interaction history (keep recent ones)
            recent_history = self.interaction_history[-1000:]  # Keep last 1000
            history_data = [record.to_dict() for record in recent_history]
            self.storage.store_data(
                'learning_logs',
                'interaction_history',
                history_data
            )
            
            # Save patterns
            self.storage.store_data(
                'learning_logs',
                'learned_patterns',
                self.learned_patterns
            )
            
            # Save preference models
            self.storage.store_data(
                'behavior_profiles',
                'preference_models',
                self.preference_models
            )
            
            # Save linguistic patterns
            self.storage.store_data(
                'behavior_profiles',
                'linguistic_patterns',
                self.linguistic_patterns
            )
            
        except Exception as e:
            print(f"Error saving learning state: {e}")
    
    def record_interaction(self, interaction_type: str, data: Dict) -> str:
        """
        Record an interaction for learning
        
        Args:
            interaction_type: Type of interaction (command, query, etc.)
            data: Interaction data
            
        Returns:
            Interaction ID
        """
        record = InteractionRecord(interaction_type, data)
        self.interaction_history.append(record)
        
        # Auto-learn if enabled and permission granted
        if (config.ENABLE_AUTO_LEARNING and 
            self.permissions.check_permission(PermissionType.AUTO_LEARNING)):
            self._auto_learn(record)
        
        # Save periodically
        if len(self.interaction_history) % 10 == 0:
            self._save_learning_state()
        
        return record.id
    
    def _auto_learn(self, record: InteractionRecord):
        """
        Automatically learn from an interaction
        
        Args:
            record: Interaction record to learn from
        """
        try:
            # Extract and learn patterns based on interaction type
            if record.type == 'command':
                self._learn_command_patterns(record)
            elif record.type == 'query':
                self._learn_query_patterns(record)
            elif record.type == 'conversation':
                self._learn_linguistic_patterns(record)
            elif record.type == 'preference':
                self._learn_preference(record)
            
            record.learned = True
            
        except Exception as e:
            print(f"Error in auto-learning: {e}")
    
    def _learn_command_patterns(self, record: InteractionRecord):
        """Learn from command interactions"""
        command = record.data.get('command', '')
        context = record.data.get('context', {})
        
        if 'command_patterns' not in self.learned_patterns:
            self.learned_patterns['command_patterns'] = {}
        
        # Track command frequency
        if command not in self.learned_patterns['command_patterns']:
            self.learned_patterns['command_patterns'][command] = {
                'count': 0,
                'contexts': [],
                'time_patterns': [],
                'success_rate': 1.0
            }
        
        pattern = self.learned_patterns['command_patterns'][command]
        pattern['count'] += 1
        pattern['contexts'].append(context)
        pattern['time_patterns'].append(record.timestamp)
        
        # Keep only recent contexts
        if len(pattern['contexts']) > 100:
            pattern['contexts'] = pattern['contexts'][-100:]
        
        # Update success rate if available
        if 'success' in record.data:
            old_rate = pattern['success_rate']
            new_rate = 1.0 if record.data['success'] else 0.0
            pattern['success_rate'] = 0.9 * old_rate + 0.1 * new_rate
    
    def _learn_query_patterns(self, record: InteractionRecord):
        """Learn from query interactions"""
        query = record.data.get('query', '')
        response = record.data.get('response', '')
        
        if 'query_patterns' not in self.learned_patterns:
            self.learned_patterns['query_patterns'] = {}
        
        # Extract keywords
        keywords = query.lower().split()[:5]  # First 5 words as key
        key = ' '.join(keywords)
        
        if key not in self.learned_patterns['query_patterns']:
            self.learned_patterns['query_patterns'][key] = {
                'count': 0,
                'responses': [],
                'satisfaction': []
            }
        
        pattern = self.learned_patterns['query_patterns'][key]
        pattern['count'] += 1
        pattern['responses'].append(response)
        
        if 'satisfaction' in record.data:
            pattern['satisfaction'].append(record.data['satisfaction'])
    
    def _learn_linguistic_patterns(self, record: InteractionRecord):
        """Learn linguistic patterns from conversation"""
        text = record.data.get('text', '')
        
        if not text:
            return
        
        # Extract linguistic features
        words = text.lower().split()
        
        # Track word usage
        if 'word_frequency' not in self.linguistic_patterns:
            self.linguistic_patterns['word_frequency'] = {}
        
        for word in words:
            if len(word) > 2:  # Skip very short words
                self.linguistic_patterns['word_frequency'][word] = \
                    self.linguistic_patterns['word_frequency'].get(word, 0) + 1
        
        # Track common phrases (bigrams)
        if 'common_phrases' not in self.linguistic_patterns:
            self.linguistic_patterns['common_phrases'] = {}
        
        for i in range(len(words) - 1):
            phrase = f"{words[i]} {words[i+1]}"
            self.linguistic_patterns['common_phrases'][phrase] = \
                self.linguistic_patterns['common_phrases'].get(phrase, 0) + 1
        
        # Track sentence structure
        if 'sentence_lengths' not in self.linguistic_patterns:
            self.linguistic_patterns['sentence_lengths'] = []
        
        sentences = text.split('.')
        for sentence in sentences:
            if sentence.strip():
                self.linguistic_patterns['sentence_lengths'].append(
                    len(sentence.split())
                )
        
        # Keep only recent data
        if len(self.linguistic_patterns['sentence_lengths']) > 1000:
            self.linguistic_patterns['sentence_lengths'] = \
                self.linguistic_patterns['sentence_lengths'][-1000:]
    
    def _learn_preference(self, record: InteractionRecord):
        """Learn user preferences"""
        preference_type = record.data.get('type', '')
        preference_value = record.data.get('value', '')
        
        if not preference_type:
            return
        
        if preference_type not in self.preference_models:
            self.preference_models[preference_type] = {
                'values': [],
                'weights': [],
                'last_updated': record.timestamp
            }
        
        model = self.preference_models[preference_type]
        
        # Add new preference with decay on old ones
        decay_factor = config.PREFERENCE_WEIGHT_DECAY
        model['weights'] = [w * decay_factor for w in model['weights']]
        
        # Add new preference
        if preference_value in model['values']:
            idx = model['values'].index(preference_value)
            model['weights'][idx] += 1.0
        else:
            model['values'].append(preference_value)
            model['weights'].append(1.0)
        
        model['last_updated'] = record.timestamp
    
    def get_learned_patterns(self, pattern_type: Optional[str] = None) -> Dict:
        """
        Get learned patterns
        
        Args:
            pattern_type: Optional filter by pattern type
            
        Returns:
            Dictionary of patterns
        """
        if pattern_type:
            return self.learned_patterns.get(pattern_type, {})
        return self.learned_patterns
    
    def get_preferences(self, preference_type: Optional[str] = None) -> Dict:
        """
        Get learned preferences
        
        Args:
            preference_type: Optional filter by preference type
            
        Returns:
            Dictionary of preferences
        """
        if preference_type:
            return self.preference_models.get(preference_type, {})
        return self.preference_models
    
    def predict_preference(self, preference_type: str, 
                          options: List[str]) -> Optional[str]:
        """
        Predict preferred option from list
        
        Args:
            preference_type: Type of preference
            options: List of possible options
            
        Returns:
            Most likely preferred option or None
        """
        if preference_type not in self.preference_models:
            return None
        
        model = self.preference_models[preference_type]
        
        # Find option with highest weight
        best_option = None
        best_weight = 0.0
        
        for option in options:
            if option in model['values']:
                idx = model['values'].index(option)
                weight = model['weights'][idx]
                if weight > best_weight:
                    best_weight = weight
                    best_option = option
        
        return best_option
    
    def predict_next_action(self, context: Dict) -> Optional[str]:
        """
        Predict next likely action based on context
        
        Args:
            context: Current context information
            
        Returns:
            Predicted action or None
        """
        # Simple prediction based on command patterns
        if 'command_patterns' not in self.learned_patterns:
            return None
        
        # Find most frequent command in similar contexts
        # This is a simplified version - production would use ML
        most_frequent = None
        max_count = 0
        
        for command, pattern in self.learned_patterns['command_patterns'].items():
            if pattern['count'] > max_count:
                max_count = pattern['count']
                most_frequent = command
        
        return most_frequent
    
    def get_linguistic_style(self) -> Dict:
        """
        Get analyzed linguistic style
        
        Returns:
            Dictionary with style characteristics
        """
        style = {
            'vocabulary_size': len(self.linguistic_patterns.get('word_frequency', {})),
            'most_common_words': [],
            'most_common_phrases': [],
            'avg_sentence_length': 0.0,
            'formality_score': 0.5,  # Placeholder
        }
        
        # Get most common words
        if 'word_frequency' in self.linguistic_patterns:
            word_freq = self.linguistic_patterns['word_frequency']
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            style['most_common_words'] = [w for w, _ in sorted_words[:20]]
        
        # Get most common phrases
        if 'common_phrases' in self.linguistic_patterns:
            phrase_freq = self.linguistic_patterns['common_phrases']
            sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)
            style['most_common_phrases'] = [p for p, _ in sorted_phrases[:20]]
        
        # Calculate average sentence length
        if 'sentence_lengths' in self.linguistic_patterns:
            lengths = self.linguistic_patterns['sentence_lengths']
            if lengths:
                style['avg_sentence_length'] = np.mean(lengths)
        
        return style
    
    def get_interaction_statistics(self) -> Dict:
        """Get statistics about interactions"""
        stats = {
            'total_interactions': len(self.interaction_history),
            'learned_interactions': sum(1 for r in self.interaction_history if r.learned),
            'by_type': {},
            'patterns_learned': len(self.learned_patterns),
            'preferences_learned': len(self.preference_models),
        }
        
        # Count by type
        for record in self.interaction_history:
            stats['by_type'][record.type] = stats['by_type'].get(record.type, 0) + 1
        
        return stats
    
    def export_learned_knowledge(self) -> Dict:
        """Export all learned knowledge for backup or analysis"""
        return {
            'learned_patterns': self.learned_patterns,
            'preference_models': self.preference_models,
            'linguistic_patterns': self.linguistic_patterns,
            'statistics': self.get_interaction_statistics(),
            'exported_at': datetime.now().isoformat()
        }
