#!/usr/bin/env python3
"""
Fetch GitHub repository statistics and save to JSON
This runs via GitHub Actions to update data regularly
"""

import os
import json
from datetime import datetime
from github import Github, Auth
import sys

# Repository URLs
REPO_URLS = [
    'https://github.com/ram4ik/DocksidePage',
    'https://github.com/ram4ik/WanderWisePage',
    'https://github.com/ram4ik/SmartExpenceTrackerPage',
    'https://github.com/ram4ik/MorseDotMessengerPage',
    'https://github.com/ram4ik/PlanistryPage',
    'https://github.com/ram4ik/SecureCubePage',
    'https://github.com/ram4ik/UinakPage',
    'https://github.com/ram4ik/TaskVibePilotPage',
    'https://github.com/ram4ik/RealLifeStoriesAIPage',
    'https://github.com/ram4ik/AegisSecurePage',
    'https://github.com/ram4ik/MySpeedometerPilotPage',
    'https://github.com/ram4ik/ScreenshotZenPage',
    'https://github.com/ram4ik/KaraokeViveProPage',
    'https://github.com/ram4ik/ESTBuddy2Page',
    'https://github.com/ram4ik/SmartQRCodeAnalyzerPage',
    'https://github.com/ram4ik/FityazeoPage',
    'https://github.com/ram4ik/VibeVoiceJournalPage',
    'https://github.com/ram4ik/DiElaMathemaPage',
    'https://github.com/ram4ik/ReceptoVibePage',
    'https://github.com/ram4ik/SmartNotetakerPage',
    'https://github.com/ram4ik/SketchPadAIPage',
    'https://github.com/ram4ik/FeelsAlivePage',
    'https://github.com/ram4ik/VibeHabitPulsePage'
]

def parse_repo_url(url):
    """Extract owner and repo from GitHub URL"""
    parts = url.replace('https://github.com/', '').split('/')
    if len(parts) >= 2:
        return {
            'owner': parts[0],
            'repo': parts[1],
            'app_name': parts[1].replace('Page', '')
        }
    return None

def fetch_repo_data(github_client, owner, repo_name):
    """Fetch all data for a repository"""
    try:
        repo = github_client.get_repo(f"{owner}/{repo_name}")

        # Get views (last 14 days)
        try:
            views = repo.get_views_traffic(per="week")
            views_data = {
                'count': views.count,
                'uniques': views.uniques,
                'views': [
                    {
                        'timestamp': view.timestamp.isoformat(),
                        'count': view.count,
                        'uniques': view.uniques
                    }
                    for view in views.views
                ]
            }
        except:
            views_data = {'count': 0, 'uniques': 0, 'views': []}

        # Get clones
        try:
            clones = repo.get_clones_traffic(per="week")
            clones_data = {
                'count': clones.count,
                'uniques': clones.uniques,
                'clones': [
                    {
                        'timestamp': clone.timestamp.isoformat(),
                        'count': clone.count,
                        'uniques': clone.uniques
                    }
                    for clone in clones.clones
                ]
            }
        except:
            clones_data = {'count': 0, 'uniques': 0, 'clones': []}

        # Get referrers
        try:
            referrers = repo.get_top_referrers()
            referrers_data = [
                {
                    'referrer': ref.referrer,
                    'count': ref.count,
                    'uniques': ref.uniques
                }
                for ref in referrers[:10]  # Top 10
            ]
        except:
            referrers_data = []

        # Get popular paths
        try:
            paths = repo.get_top_paths()
            paths_data = [
                {
                    'path': path.path,
                    'title': path.title,
                    'count': path.count,
                    'uniques': path.uniques
                }
                for path in paths[:10]  # Top 10
            ]
        except:
            paths_data = []

        # Basic repo info
        repo_info = {
            'name': repo.name,
            'full_name': repo.full_name,
            'description': repo.description,
            'url': repo.html_url,
            'stars': repo.stargazers_count,
            'forks': repo.forks_count,
            'watchers': repo.watchers_count,
            'open_issues': repo.open_issues_count,
            'language': repo.language,
            'created_at': repo.created_at.isoformat(),
            'updated_at': repo.updated_at.isoformat(),
            'pushed_at': repo.pushed_at.isoformat() if repo.pushed_at else None,
            'size': repo.size,
            'default_branch': repo.default_branch,
            'topics': repo.get_topics() if hasattr(repo, 'get_topics') else []
        }

        return {
            'info': repo_info,
            'views': views_data,
            'clones': clones_data,
            'referrers': referrers_data,
            'paths': paths_data,
            'success': True
        }

    except Exception as e:
        print(f"Error fetching {owner}/{repo_name}: {str(e)}")
        return {
            'info': {
                'name': repo_name,
                'full_name': f"{owner}/{repo_name}",
                'error': str(e)
            },
            'success': False
        }

def main():
    # Get GitHub token
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("ERROR: GITHUB_TOKEN not found in environment")
        sys.exit(1)

    # Initialize GitHub client
    auth = Auth.Token(token)
    github_client = Github(auth=auth)

    print("Fetching data for all repositories...")

    # Parse repos
    repos = [parse_repo_url(url) for url in REPO_URLS]
    repos = [r for r in repos if r is not None]

    # Fetch data
    all_data = {}
    total_stats = {
        'total_apps': 0,
        'total_stars': 0,
        'total_forks': 0,
        'total_watchers': 0,
        'total_views_14d': 0,
        'total_unique_visitors_14d': 0,
        'total_clones_14d': 0
    }

    for repo_info in repos:
        app_name = repo_info['app_name']
        print(f"Fetching: {app_name}...")

        data = fetch_repo_data(
            github_client,
            repo_info['owner'],
            repo_info['repo']
        )

        if data['success']:
            all_data[app_name] = data
            total_stats['total_apps'] += 1
            total_stats['total_stars'] += data['info']['stars']
            total_stats['total_forks'] += data['info']['forks']
            total_stats['total_watchers'] += data['info']['watchers']
            total_stats['total_views_14d'] += data['views']['count']
            total_stats['total_unique_visitors_14d'] += data['views']['uniques']
            total_stats['total_clones_14d'] += data['clones']['count']

    # Create output
    output = {
        'last_updated': datetime.utcnow().isoformat() + 'Z',
        'total_stats': total_stats,
        'apps': all_data
    }

    # Save to JSON
    os.makedirs('data', exist_ok=True)
    with open('data/stats.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n✅ Successfully fetched data for {total_stats['total_apps']} apps")
    print(f"📊 Total stats: {total_stats['total_stars']} stars, {total_stats['total_views_14d']} views (14d)")
    print(f"💾 Data saved to data/stats.json")

if __name__ == '__main__':
    main()
