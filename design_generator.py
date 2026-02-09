"""
AMRIT AI Design Generation System
Automatically generates designs, UI/UX, branding based on user preferences
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
import amrit_config as config
from secure_storage import secure_storage


class DesignGenerator:
    """
    Auto-design generation system for AMRIT AI
    Creates designs, UI/UX, branding, and visual assets
    """
    
    def __init__(self):
        self.design_history = []
        self._load_preferences()
    
    def _load_preferences(self):
        """Load user's design preferences"""
        self.design_preferences = secure_storage.load_preference('design_style') or {
            'color_scheme': 'modern',
            'style': 'minimalist',
            'preferred_colors': ['#2563eb', '#7c3aed', '#db2777'],
            'typography': 'sans-serif',
            'layout_preference': 'clean'
        }
    
    def generate_design(self, 
                       design_type: str,
                       description: str,
                       style_hints: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate design based on requirements
        
        Args:
            design_type: Type of design (Logo, UI/UX, Brand Identity, etc.)
            description: Description of design requirements
            style_hints: Optional style hints and preferences
        
        Returns:
            Generated design data
        """
        if design_type not in config.DESIGN_CATEGORIES:
            return {
                'success': False,
                'error': f'Design type {design_type} not supported. Supported: {config.DESIGN_CATEGORIES}'
            }
        
        # Merge user preferences with style hints
        design_style = {**self.design_preferences, **(style_hints or {})}
        
        # Generate design based on type
        design_generators = {
            'Logo': self._generate_logo_design,
            'Brand Identity': self._generate_brand_identity,
            'UI/UX': self._generate_ui_ux_design,
            'Color Scheme': self._generate_color_scheme,
            'Typography': self._generate_typography,
            'Layout': self._generate_layout_design,
            'Icons': self._generate_icon_set,
            'Illustrations': self._generate_illustrations
        }
        
        generator = design_generators.get(design_type, self._generate_generic_design)
        design_result = generator(description, design_style)
        
        # Save design to storage
        design_data = {
            'design_type': design_type,
            'description': description,
            'style': design_style,
            'design': design_result
        }
        
        design_id = secure_storage.save_design(description[:50], design_data)
        
        # Update design history
        self.design_history.append({
            'design_id': design_id,
            'design_type': design_type,
            'description': description,
            'timestamp': datetime.now().isoformat()
        })
        
        # Learn from this design
        self._learn_from_design(design_type, design_style)
        
        return {
            'success': True,
            'design_id': design_id,
            'design_type': design_type,
            'design': design_result,
            'message': f'✅ {design_type} generated successfully!'
        }
    
    def _generate_logo_design(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate logo design"""
        
        primary_color = style.get('preferred_colors', ['#2563eb'])[0]
        
        logo_design = {
            'name': description,
            'concept': 'Modern, minimalist logo design',
            'primary_color': primary_color,
            'secondary_color': style.get('preferred_colors', ['#2563eb', '#7c3aed'])[1] if len(style.get('preferred_colors', [])) > 1 else '#7c3aed',
            'typography': style.get('typography', 'sans-serif'),
            'style': style.get('style', 'minimalist'),
            'svg_template': f'''
<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="80" fill="{primary_color}" opacity="0.2"/>
    <text x="100" y="100" text-anchor="middle" font-size="60" font-family="{style.get('typography', 'sans-serif')}" fill="{primary_color}">
        {description[0].upper()}
    </text>
</svg>
''',
            'usage_notes': [
                'Scalable vector format',
                'Works on light and dark backgrounds',
                'Can be customized for different sizes'
            ]
        }
        
        return logo_design
    
    def _generate_brand_identity(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate complete brand identity"""
        
        colors = style.get('preferred_colors', ['#2563eb', '#7c3aed', '#db2777'])
        
        brand_identity = {
            'brand_name': description,
            'tagline': f'Powered by AMRIT AI - {description}',
            'color_palette': {
                'primary': colors[0] if len(colors) > 0 else '#2563eb',
                'secondary': colors[1] if len(colors) > 1 else '#7c3aed',
                'accent': colors[2] if len(colors) > 2 else '#db2777',
                'background': '#ffffff',
                'text': '#1f2937'
            },
            'typography': {
                'headings': 'Inter, system-ui, sans-serif',
                'body': 'Inter, system-ui, sans-serif',
                'code': 'JetBrains Mono, monospace'
            },
            'logo': self._generate_logo_design(description, style),
            'voice_tone': 'Professional, innovative, user-friendly',
            'values': [
                'Innovation',
                'User Privacy',
                'Continuous Learning',
                'Excellence'
            ]
        }
        
        return brand_identity
    
    def _generate_ui_ux_design(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate UI/UX design"""
        
        colors = style.get('preferred_colors', ['#2563eb', '#7c3aed'])
        
        ui_ux_design = {
            'project_name': description,
            'design_system': {
                'colors': {
                    'primary': colors[0] if len(colors) > 0 else '#2563eb',
                    'secondary': colors[1] if len(colors) > 1 else '#7c3aed',
                    'success': '#10b981',
                    'warning': '#f59e0b',
                    'error': '#ef4444',
                    'neutral': '#6b7280'
                },
                'spacing': {
                    'xs': '4px',
                    'sm': '8px',
                    'md': '16px',
                    'lg': '24px',
                    'xl': '32px'
                },
                'typography': {
                    'heading_1': {'size': '2.5rem', 'weight': 'bold'},
                    'heading_2': {'size': '2rem', 'weight': 'semibold'},
                    'heading_3': {'size': '1.5rem', 'weight': 'semibold'},
                    'body': {'size': '1rem', 'weight': 'normal'},
                    'small': {'size': '0.875rem', 'weight': 'normal'}
                },
                'border_radius': {
                    'sm': '4px',
                    'md': '8px',
                    'lg': '12px',
                    'full': '9999px'
                }
            },
            'layout': {
                'type': style.get('layout_preference', 'clean'),
                'grid_columns': 12,
                'max_width': '1200px',
                'responsive_breakpoints': {
                    'mobile': '640px',
                    'tablet': '768px',
                    'desktop': '1024px',
                    'wide': '1280px'
                }
            },
            'components': [
                'Navigation Bar',
                'Hero Section',
                'Content Cards',
                'Form Elements',
                'Buttons',
                'Footer'
            ],
            'user_flow': [
                'Landing Page',
                'Authentication',
                'Dashboard',
                'Feature Pages',
                'Settings'
            ]
        }
        
        return ui_ux_design
    
    def _generate_color_scheme(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate color scheme"""
        
        base_colors = style.get('preferred_colors', ['#2563eb', '#7c3aed', '#db2777'])
        
        color_scheme = {
            'name': f'{description} Color Palette',
            'primary_colors': base_colors,
            'shades': {
                'primary': {
                    '50': self._lighten_color(base_colors[0], 0.9),
                    '100': self._lighten_color(base_colors[0], 0.8),
                    '500': base_colors[0],
                    '700': self._darken_color(base_colors[0], 0.2),
                    '900': self._darken_color(base_colors[0], 0.4)
                }
            },
            'usage_guide': {
                'primary': 'Main actions, links, brand elements',
                'secondary': 'Supporting actions, accents',
                'accent': 'Call-to-action, highlights',
                'neutral': 'Text, borders, backgrounds'
            }
        }
        
        return color_scheme
    
    def _lighten_color(self, color: str, amount: float) -> str:
        """Lighten a hex color (simplified)"""
        # In real implementation, would properly convert and lighten
        return color  # Placeholder
    
    def _darken_color(self, color: str, amount: float) -> str:
        """Darken a hex color (simplified)"""
        # In real implementation, would properly convert and darken
        return color  # Placeholder
    
    def _generate_typography(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate typography system"""
        
        typography = {
            'font_pairings': {
                'primary': 'Inter',
                'secondary': 'Roboto',
                'accent': 'Playfair Display',
                'monospace': 'JetBrains Mono'
            },
            'type_scale': {
                'xs': '0.75rem',
                'sm': '0.875rem',
                'base': '1rem',
                'lg': '1.125rem',
                'xl': '1.25rem',
                '2xl': '1.5rem',
                '3xl': '1.875rem',
                '4xl': '2.25rem',
                '5xl': '3rem'
            },
            'line_heights': {
                'tight': 1.25,
                'normal': 1.5,
                'relaxed': 1.75
            },
            'weights': {
                'light': 300,
                'normal': 400,
                'medium': 500,
                'semibold': 600,
                'bold': 700
            }
        }
        
        return typography
    
    def _generate_layout_design(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate layout design"""
        
        layout = {
            'type': style.get('layout_preference', 'clean'),
            'structure': {
                'header': {
                    'height': '64px',
                    'position': 'sticky',
                    'components': ['Logo', 'Navigation', 'User Menu']
                },
                'main': {
                    'max_width': '1200px',
                    'padding': '24px',
                    'sections': ['Hero', 'Features', 'Content', 'CTA']
                },
                'sidebar': {
                    'width': '256px',
                    'position': 'fixed',
                    'components': ['Navigation', 'Quick Actions']
                },
                'footer': {
                    'height': 'auto',
                    'sections': ['Links', 'Social', 'Copyright']
                }
            },
            'grid_system': {
                'columns': 12,
                'gutter': '24px',
                'container_padding': '16px'
            }
        }
        
        return layout
    
    def _generate_icon_set(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate icon set"""
        
        icon_set = {
            'style': style.get('style', 'minimalist'),
            'size_variants': ['16px', '24px', '32px', '48px'],
            'stroke_width': '2px',
            'icons': [
                'home', 'user', 'settings', 'search', 'menu',
                'close', 'check', 'arrow-right', 'arrow-left',
                'upload', 'download', 'edit', 'delete', 'save'
            ],
            'format': 'SVG',
            'usage': 'Scalable icons for UI elements'
        }
        
        return icon_set
    
    def _generate_illustrations(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate illustrations"""
        
        illustrations = {
            'style': style.get('style', 'minimalist'),
            'color_palette': style.get('preferred_colors', ['#2563eb', '#7c3aed']),
            'themes': [
                'Hero section illustration',
                'Empty state illustration',
                'Error page illustration',
                'Success confirmation illustration'
            ],
            'format': 'SVG',
            'customizable': True
        }
        
        return illustrations
    
    def _generate_generic_design(self, description: str, style: Dict[str, Any]) -> Dict[str, Any]:
        """Generate generic design"""
        
        return {
            'description': description,
            'style': style,
            'note': 'Custom design generated based on preferences'
        }
    
    def _learn_from_design(self, design_type: str, style: Dict[str, Any]):
        """Learn from design generation to improve future designs"""
        
        pattern_data = {
            'design_type': design_type,
            'style': style
        }
        
        secure_storage.save_learned_pattern('design_generation', pattern_data)
        
        # Update design preferences if new patterns detected
        self.design_preferences.update({
            'last_design_type': design_type,
            'updated_at': datetime.now().isoformat()
        })
        secure_storage.save_preference('design_style', self.design_preferences)
    
    def get_design_history(self) -> List[Dict[str, Any]]:
        """Get history of design generations"""
        return self.design_history
    
    def customize_design(self, design_id: str, customizations: Dict[str, Any]) -> Dict[str, Any]:
        """Customize an existing design"""
        
        design_data = secure_storage.load_design(design_id)
        
        if not design_data:
            return {
                'success': False,
                'error': 'Design not found'
            }
        
        # Apply customizations
        design_data['design'].update(customizations)
        design_data['customized_at'] = datetime.now().isoformat()
        
        # Save updated design
        secure_storage.save_design(design_data['description'], design_data)
        
        return {
            'success': True,
            'message': 'Design customized successfully',
            'design': design_data['design']
        }


# Global design generator instance
design_generator = DesignGenerator()
