"""
AMRIT AI - Personalized UI Generator

Generates customized UI/UX based on user preferences and patterns.
"""

import random
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import config
from hidden_storage import HiddenStorageManager


class UIPersonalizationEngine:
    """Generates personalized UI/UX elements"""
    
    def __init__(self, storage_manager: HiddenStorageManager):
        """
        Initialize UI personalization engine
        
        Args:
            storage_manager: Hidden storage manager
        """
        self.storage = storage_manager
        self.current_theme = None
        self.custom_commands = {}
        self.dashboard_config = None
        self._load_ui_config()
    
    def _load_ui_config(self):
        """Load UI configuration from storage"""
        try:
            theme_data = self.storage.retrieve_data(
                'behavior_profiles',
                'ui_theme'
            )
            if theme_data:
                self.current_theme = theme_data
            
            commands_data = self.storage.retrieve_data(
                'behavior_profiles',
                'custom_commands'
            )
            if commands_data:
                self.custom_commands = commands_data
            
            dashboard_data = self.storage.retrieve_data(
                'behavior_profiles',
                'dashboard_config'
            )
            if dashboard_data:
                self.dashboard_config = dashboard_data
        except:
            pass
    
    def _save_ui_config(self):
        """Save UI configuration to storage"""
        if self.current_theme:
            self.storage.store_data(
                'behavior_profiles',
                'ui_theme',
                self.current_theme
            )
        
        if self.custom_commands:
            self.storage.store_data(
                'behavior_profiles',
                'custom_commands',
                self.custom_commands
            )
        
        if self.dashboard_config:
            self.storage.store_data(
                'behavior_profiles',
                'dashboard_config',
                self.dashboard_config
            )
    
    def generate_color_theme(self, preferences: Dict) -> Dict:
        """
        Generate color theme based on preferences
        
        Args:
            preferences: User preference dictionary
            
        Returns:
            Color theme dictionary
        """
        # Extract emotional profile for color selection
        emotional_profile = preferences.get('emotional_profile', {})
        sentiment = emotional_profile.get('overall_sentiment', 'neutral')
        
        # Base color schemes
        color_schemes = {
            'positive': {
                'primary': '#4CAF50',  # Green
                'secondary': '#8BC34A',
                'accent': '#CDDC39',
                'background': '#F1F8E9',
                'text': '#33691E'
            },
            'neutral': {
                'primary': '#2196F3',  # Blue
                'secondary': '#03A9F4',
                'accent': '#00BCD4',
                'background': '#E3F2FD',
                'text': '#0D47A1'
            },
            'negative': {
                'primary': '#9C27B0',  # Purple (calming)
                'secondary': '#BA68C8',
                'accent': '#CE93D8',
                'background': '#F3E5F5',
                'text': '#4A148C'
            }
        }
        
        theme = color_schemes.get(sentiment, color_schemes['neutral']).copy()
        theme['generated_at'] = datetime.now().isoformat()
        theme['based_on'] = sentiment
        
        return theme
    
    def generate_logo_concept(self, preferences: Dict) -> Dict:
        """
        Generate logo concept based on user patterns
        
        Args:
            preferences: User preference dictionary
            
        Returns:
            Logo concept dictionary
        """
        # Extract characteristics
        communication_style = preferences.get('preferences', {}).get('communication', {})
        technical = communication_style.get('technical_vocabulary', False)
        
        logo_concepts = {
            'technical': {
                'style': 'geometric',
                'elements': ['circuit', 'brain', 'network'],
                'shape': 'angular',
                'complexity': 'high'
            },
            'creative': {
                'style': 'organic',
                'elements': ['flower', 'wave', 'spiral'],
                'shape': 'curved',
                'complexity': 'medium'
            },
            'balanced': {
                'style': 'minimalist',
                'elements': ['circle', 'square', 'triangle'],
                'shape': 'simple',
                'complexity': 'low'
            }
        }
        
        if technical:
            concept = logo_concepts['technical']
        else:
            concept = logo_concepts['balanced']
        
        concept['generated_at'] = datetime.now().isoformat()
        concept['initials'] = 'AMRIT'
        
        return concept
    
    def generate_custom_commands(self, learned_patterns: Dict) -> Dict:
        """
        Generate custom commands based on learned patterns
        
        Args:
            learned_patterns: Dictionary of learned patterns
            
        Returns:
            Dictionary of custom commands
        """
        custom_commands = {}
        
        # Get command patterns
        command_patterns = learned_patterns.get('command_patterns', {})
        
        # Create shortcuts for frequently used commands
        for command, pattern in command_patterns.items():
            if pattern['count'] > 10:  # Frequently used
                # Generate shortcut
                words = command.split()
                if len(words) > 1:
                    shortcut = ''.join([w[0] for w in words[:3]])
                    custom_commands[shortcut] = {
                        'full_command': command,
                        'usage_count': pattern['count'],
                        'created_at': datetime.now().isoformat()
                    }
        
        return custom_commands
    
    def generate_dashboard_layout(self, preferences: Dict) -> Dict:
        """
        Generate personalized dashboard layout
        
        Args:
            preferences: User preference dictionary
            
        Returns:
            Dashboard configuration
        """
        # Extract relevant preferences
        time_patterns = preferences.get('patterns', {}).get('time', {})
        command_prefs = preferences.get('preferences', {}).get('command_style', [])
        
        # Generate widget configuration
        widgets = []
        
        # Time-based widgets
        active_hours = time_patterns.get('active_hours', [])
        if active_hours:
            widgets.append({
                'type': 'activity_timeline',
                'position': 'top',
                'data': active_hours
            })
        
        # Command shortcuts
        if command_prefs:
            widgets.append({
                'type': 'quick_commands',
                'position': 'left',
                'commands': command_prefs
            })
        
        # Status widget
        widgets.append({
            'type': 'system_status',
            'position': 'top-right',
            'show': ['health', 'learning_progress', 'permissions']
        })
        
        # Recent interactions
        widgets.append({
            'type': 'recent_activity',
            'position': 'center',
            'limit': 10
        })
        
        dashboard = {
            'layout': 'adaptive',
            'widgets': widgets,
            'generated_at': datetime.now().isoformat(),
            'version': '1.0'
        }
        
        return dashboard
    
    def generate_ui_preferences(self, preferences: Dict) -> Dict:
        """
        Generate complete UI preference configuration
        
        Args:
            preferences: User preference dictionary
            
        Returns:
            Complete UI configuration
        """
        ui_config = {
            'theme': self.generate_color_theme(preferences),
            'typography': self._generate_typography(preferences),
            'layout': self._generate_layout_preferences(preferences),
            'interactions': self._generate_interaction_preferences(preferences),
            'generated_at': datetime.now().isoformat()
        }
        
        return ui_config
    
    def _generate_typography(self, preferences: Dict) -> Dict:
        """Generate typography preferences"""
        communication = preferences.get('preferences', {}).get('communication', {})
        complexity = communication.get('sentence_complexity', 'medium')
        
        typography = {
            'font_family': 'Inter, system-ui, sans-serif',
            'base_size': '16px',
            'line_height': '1.5',
            'heading_scale': 1.25
        }
        
        # Adjust based on complexity preference
        if complexity == 'simple':
            typography['base_size'] = '18px'
            typography['line_height'] = '1.6'
        elif complexity == 'complex':
            typography['base_size'] = '14px'
            typography['line_height'] = '1.4'
        
        return typography
    
    def _generate_layout_preferences(self, preferences: Dict) -> Dict:
        """Generate layout preferences"""
        response_prefs = preferences.get('preferences', {}).get('response_style', {})
        preferred_length = response_prefs.get('preferred_length', 'medium')
        
        layout = {
            'sidebar': 'left',
            'content_width': '800px',
            'spacing': 'comfortable',
            'density': 'medium'
        }
        
        # Adjust based on content preferences
        if preferred_length == 'brief':
            layout['content_width'] = '600px'
            layout['density'] = 'compact'
        elif preferred_length == 'detailed':
            layout['content_width'] = '1000px'
            layout['spacing'] = 'spacious'
        
        return layout
    
    def _generate_interaction_preferences(self, preferences: Dict) -> Dict:
        """Generate interaction preferences"""
        decision_patterns = preferences.get('patterns', {}).get('decision', {})
        decision_speed = decision_patterns.get('decision_speed', 'moderate')
        
        interactions = {
            'animation_speed': 'normal',
            'confirmation_dialogs': True,
            'keyboard_shortcuts': True,
            'auto_complete': True
        }
        
        # Adjust based on decision speed
        if decision_speed == 'fast':
            interactions['animation_speed'] = 'fast'
            interactions['confirmation_dialogs'] = False
        elif decision_speed == 'deliberate':
            interactions['animation_speed'] = 'slow'
            interactions['confirmation_dialogs'] = True
        
        return interactions
    
    def create_personalized_ui(self, personalization_profile: Dict, 
                              learned_patterns: Dict) -> Dict:
        """
        Create complete personalized UI configuration
        
        Args:
            personalization_profile: User personalization profile
            learned_patterns: Learned patterns dictionary
            
        Returns:
            Complete personalized UI configuration
        """
        ui_package = {
            'theme': self.generate_color_theme(personalization_profile),
            'logo': self.generate_logo_concept(personalization_profile),
            'custom_commands': self.generate_custom_commands(learned_patterns),
            'dashboard': self.generate_dashboard_layout(personalization_profile),
            'preferences': self.generate_ui_preferences(personalization_profile),
            'generated_at': datetime.now().isoformat(),
            'version': '1.0.0'
        }
        
        # Save configuration
        self.current_theme = ui_package['theme']
        self.custom_commands = ui_package['custom_commands']
        self.dashboard_config = ui_package['dashboard']
        self._save_ui_config()
        
        return ui_package
    
    def get_current_theme(self) -> Optional[Dict]:
        """Get current UI theme"""
        return self.current_theme
    
    def get_custom_commands(self) -> Dict:
        """Get custom commands"""
        return self.custom_commands
    
    def get_dashboard_config(self) -> Optional[Dict]:
        """Get dashboard configuration"""
        return self.dashboard_config
    
    def update_theme_color(self, color_key: str, color_value: str):
        """
        Update a specific theme color
        
        Args:
            color_key: Color property key
            color_value: Hex color value
        """
        if self.current_theme:
            self.current_theme[color_key] = color_value
            self.current_theme['last_updated'] = datetime.now().isoformat()
            self._save_ui_config()
    
    def add_custom_command(self, shortcut: str, command: str):
        """
        Add a custom command shortcut
        
        Args:
            shortcut: Shortcut key
            command: Full command
        """
        self.custom_commands[shortcut] = {
            'full_command': command,
            'usage_count': 0,
            'created_at': datetime.now().isoformat()
        }
        self._save_ui_config()
