// resource_id: "e645c11b-3c02-4d49-92cb-2f58b7f44ba6"
// resource_type: "document"
// resource_name: "firebase-config"
// Initialize Firebase using CDN (loaded in HTML)
// Firebase is loaded via CDN in the HTML template
const app = firebase.initializeApp(window.FIREBASE_CONFIG);
const auth = firebase.auth();
const googleProvider = new firebase.auth.GoogleAuthProvider();

// Connect to Firebase emulators in development
// Only use emulators if authDomain is 'localhost' (indicating dev mode is intended)
if (window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.authDomain === 'localhost') {
    console.log('🔧 Development mode: Connecting to Firebase emulators');
    try {
        auth.useEmulator('http://localhost:9099');
        console.log('✅ Connected to Firebase Auth emulator');
    } catch (error) {
        console.warn('⚠️ Could not connect to Firebase Auth emulator:', error);
        console.log('Using production Firebase instead');
    }
}

// Configure Google OAuth scopes
googleProvider.addScope('email');
googleProvider.addScope('profile');

// Export for use in other scripts
window.firebaseAuth = {
    auth: auth,
    signInWithEmail: (email, password) => {
        return auth.signInWithEmailAndPassword(email, password)
            .then((userCredential) => {
                const user = userCredential.user;
                console.log('Email sign-in successful:', user);
                
                // Send the user data to the server
                return fetch('/auth/email', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        uid: user.uid,
                        email: user.email,
                        displayName: user.displayName || user.email.split('@')[0],
                        photoURL: user.photoURL || ''
                    })
                }).then(response => {
                    if (response.ok) {
                        console.log('Server authentication successful, redirecting to dashboard');
                        window.location.href = '/dashboard';
                    } else {
                        console.error('Server authentication failed:', response.status);
                        throw new Error('Server authentication failed');
                    }
                });
            })
            .catch((error) => {
                console.error('Email sign-in error:', error);
                throw error;
            });
    },
    signUpWithEmail: (email, password, username) => {
        return auth.createUserWithEmailAndPassword(email, password)
            .then((userCredential) => {
                const user = userCredential.user;
                console.log('Email sign-up successful:', user);
                
                // Update the user's display name
                return user.updateProfile({
                    displayName: username
                }).then(() => {
                    // Send the user data to the server
                    return fetch('/auth/email', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            uid: user.uid,
                            email: user.email,
                            displayName: username,
                            photoURL: user.photoURL || ''
                        })
                    }).then(response => {
                        if (response.ok) {
                            console.log('Server authentication successful, redirecting to dashboard');
                            window.location.href = '/dashboard';
                        } else {
                            console.error('Server authentication failed:', response.status);
                            throw new Error('Server authentication failed');
                        }
                    });
                });
            })
            .catch((error) => {
                console.error('Email sign-up error:', error);
                throw error;
            });
    },
    signInWithGoogle: () => {
        return auth.signInWithPopup(googleProvider)
            .then((result) => {
                const user = result.user;
                console.log('Google sign-in successful:', user);
                
                // In emulator mode, credential might be null, so we handle it gracefully
                const credential = firebase.auth.GoogleAuthProvider.credentialFromResult(result);
                const token = credential ? credential.accessToken : null;
                const idToken = result._tokenResponse ? result._tokenResponse.idToken : null;
                
                // Send the user data to the server
                return fetch('/auth/google', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        idToken: idToken || 'emulator_token',
                        accessToken: token,
                        user: {
                            uid: user.uid,
                            email: user.email,
                            displayName: user.displayName,
                            photoURL: user.photoURL
                        }
                    })
                }).then(response => {
                    return response.json().then(data => {
                        if (response.ok && data.success) {
                            console.log('Server authentication successful:', data.message);
                            console.log('Redirecting to dashboard');
                            window.location.href = '/dashboard';
                        } else {
                            console.error('Server authentication failed:', data.error || 'Unknown error');
                            throw new Error(data.error || 'Server authentication failed');
                        }
                    }).catch(jsonError => {
                        console.error('Failed to parse response:', jsonError);
                        throw new Error('Invalid server response');
                    });
                });
            })
            .catch((error) => {
                console.error('Google sign-in error:', error);
                // Show error to user
                alert('Login failed: ' + (error.message || error));
                // Re-enable the button on error
                const button = document.getElementById('google-signin-btn');
                if (button) {
                    button.disabled = false;
                    button.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24"><path fill="white" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="white" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="white" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/><path fill="white" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/></svg>Sign in with Google';
                }
                throw error;
            });
    }
};
