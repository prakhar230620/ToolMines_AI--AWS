from flask import render_template, session, redirect, url_for
from functools import wraps
from urllib.parse import urlencode

def all_tool_routes(app, auth_required=None, track_tool_usage=None):
    @app.route('/chatbot')
    @auth_required if auth_required else lambda f: f
    def chatbot_page():
        if track_tool_usage:
            track_tool_usage('CHAT001', session.get('user_id'))
            
        # Add user_id and session data to redirect URL
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))
            
        params = {
            'user_id': user_id,
            'session_token': session.get('_id', '')  # Add a session token if you have one
        }
        
        # Use your Vercel deployment URL in production
        
        base_url = "https://toolminesai1-360zlk7m0-commanders-projects-afe5d523.vercel.app"
    
            
        redirect_url = f'{base_url}?{urlencode(params)}'
        return redirect(redirect_url)


    @app.route('/voicebot')
    @auth_required if auth_required else lambda f: f
    def voicebot():
        if track_tool_usage:
            track_tool_usage('VOICE001', session.get('user_id'))

        # Add user_id and session data to redirect URL
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))
            
        params = {
            'user_id': user_id,
            'session_token': session.get('_id', '')  # Add a session token if you have one
        }
        
        # Use your Vercel deployment URL in production
        
        base_url = 'http://127.0.0.1:8081'
    
            
        redirect_url = f'{base_url}?{urlencode(params)}'
        return redirect(redirect_url)


    @app.route('/converter')
    @auth_required if auth_required else lambda f: f
    def converter():
        if track_tool_usage:
            track_tool_usage('CONV001', session.get('user_id'))

        # Add user_id and session data to redirect URL
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))
            
        params = {
            'user_id': user_id,
            'session_token': session.get('_id', '')  # Add a session token if you have one
        }
        
        # Use your Vercel deployment URL in production
        
        base_url = 'http://127.0.0.1:8082'
    
            
        redirect_url = f'{base_url}?{urlencode(params)}'
        return redirect(redirect_url)


    @app.route('/lang_trans')
    @auth_required if auth_required else lambda f: f
    def lang_trans():
        if track_tool_usage:
            track_tool_usage('TRANS001', session.get('user_id'))

        # Add user_id and session data to redirect URL
        user_id = session.get('user_id')
        if not user_id:
            return redirect(url_for('auth.login'))
            
        params = {
            'user_id': user_id,
            'session_token': session.get('_id', '')  # Add a session token if you have one
        }
        
        # Use your Vercel deployment URL in production
        
        base_url = 'http://127.0.0.1:8083'
    
            
        redirect_url = f'{base_url}?{urlencode(params)}'
        return redirect(redirect_url)