#!/usr/bin/env python3
"""
AMRIT AI Command Line Interface
Interactive CLI for AMRIT AI system
"""

import sys
import argparse
from datetime import datetime
from amrit_ai import amrit


def print_banner():
    """Print AMRIT AI banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║       🔮 AMRIT AI - Adaptive Multi-Realm Intelligence        ║
║                   Complete Autonomous System                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def interactive_mode():
    """Run AMRIT AI in interactive mode"""
    print_banner()
    print(f"\n👤 Welcome, {amrit.user_name}!")
    print("\n💡 Enter your commands (or 'exit' to quit, 'help' for commands)")
    print("="*60)
    
    while True:
        try:
            # Get user input
            command = input(f"\n{amrit.user_name} > ").strip()
            
            if not command:
                continue
            
            # Check for exit commands
            if command.lower() in ['exit', 'quit', 'bye']:
                amrit.shutdown()
                break
            
            # Process command
            result = amrit.process_voice_command(command)
            
            # Display result
            if result.get('success'):
                print("\n✅ SUCCESS")
                
                # Show relevant output based on command type
                if 'code' in result:
                    print("\n📝 Generated Code:")
                    print("-" * 60)
                    code = result['code']
                    # Show first 20 lines
                    lines = code.split('\n')[:20]
                    print('\n'.join(lines))
                    if len(code.split('\n')) > 20:
                        print("... (truncated)")
                    print("-" * 60)
                    
                    if result.get('instructions'):
                        print("\n📋 Instructions:")
                        print(result['instructions'])
                    
                    if result.get('files'):
                        print(f"\n📁 Files generated: {len(result['files'])}")
                        for filename in result['files'].keys():
                            print(f"  - {filename}")
                
                elif 'design' in result:
                    print("\n🎨 Design Generated:")
                    design = result['design']
                    print(f"  Type: {result.get('design_type', 'N/A')}")
                    
                    # Show design details based on type
                    if isinstance(design, dict):
                        for key, value in list(design.items())[:5]:
                            print(f"  {key}: {value}")
                
                elif 'suggestions' in result:
                    suggestions = result.get('suggestions', {}).get('suggestions', [])
                    if suggestions:
                        print("\n💡 Suggestions:")
                        for i, sug in enumerate(suggestions, 1):
                            print(f"\n  {i}. {sug['suggestion']}")
                            print(f"     💭 {sug['reason']}")
                            print(f"     🎯 Confidence: {sug['confidence']*100:.0f}%")
                    else:
                        print("\n💡 No suggestions available yet. Keep using the system to build patterns!")
                
                elif 'voice_learning' in result:
                    # Status display
                    pass
                
                if result.get('message'):
                    print(f"\n💬 {result['message']}")
            
            else:
                print("\n❌ ERROR")
                if result.get('error'):
                    print(f"  {result['error']}")
                if result.get('message'):
                    print(f"  {result['message']}")
                
                # Show suggestions if available
                if result.get('suggestions'):
                    print("\n💡 Did you mean:")
                    for sug in result['suggestions'][:3]:
                        print(f"  - {sug['suggestion']}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Shutting down...")
            amrit.shutdown()
            break
        
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again or type 'help' for assistance.")


def command_mode(command: str):
    """Run a single command"""
    print_banner()
    result = amrit.process_voice_command(command)
    
    if result.get('success'):
        print("\n✅ Command executed successfully")
        
        # For code generation, show project ID
        if result.get('project_id'):
            print(f"Project ID: {result['project_id']}")
        
        # For design generation, show design ID
        if result.get('design_id'):
            print(f"Design ID: {result['design_id']}")
        
        if result.get('message'):
            print(f"\n{result['message']}")
    else:
        print("\n❌ Command failed")
        if result.get('error'):
            print(f"Error: {result['error']}")
        sys.exit(1)


def show_status():
    """Show system status"""
    print_banner()
    result = amrit.process_voice_command('show status')
    
    if result.get('success'):
        print("\n📊 AMRIT AI System Status")
        print("="*60)
        
        voice = result['voice_learning']
        print(f"\n🎤 Voice Learning:")
        print(f"  Phase: {voice['current_phase']}")
        print(f"  Samples: {voice['samples_collected']}")
        print(f"  Progress: {voice['progress_percentage']:.1f}%")
        print(f"  Identified: {'Yes' if voice['user_identified'] else 'No'}")
        
        learning = result['learning_progress']
        print(f"\n🧠 Learning System:")
        print(f"  Phase: {learning['current_phase']}")
        print(f"  Progress: {learning['progress_percentage']:.1f}%")
        print(f"  Total Interactions: {learning['statistics']['total_interactions']}")
        print(f"  Patterns Learned: {learning['statistics']['patterns_learned']}")
        
        vault = result['vault_status']
        print(f"\n🔐 Secure Vault:")
        print(f"  Security: {vault['security_level']}")
        print(f"  Encrypted: {'Yes' if vault['encrypted'] else 'No'}")
        print(f"  Voice Biometrics: {vault['voice_biometrics_count']}")
        print(f"  Projects: {vault['projects_count']}")
        print(f"  Designs: {vault['designs_count']}")
        
        print("\n" + "="*60)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='AMRIT AI - Adaptive Multi-Realm Intelligence Technology',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python amrit_cli.py
  
  # Run single command
  python amrit_cli.py --command "Create a Python website"
  
  # Show system status
  python amrit_cli.py --status
  
  # Show help
  python amrit_cli.py --command "help"
        """
    )
    
    parser.add_argument(
        '-c', '--command',
        type=str,
        help='Run a single command'
    )
    
    parser.add_argument(
        '-s', '--status',
        action='store_true',
        help='Show system status'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'AMRIT AI v{amrit.version}'
    )
    
    args = parser.parse_args()
    
    try:
        if args.status:
            show_status()
        elif args.command:
            command_mode(args.command)
        else:
            interactive_mode()
    
    except Exception as e:
        print(f"\n❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
