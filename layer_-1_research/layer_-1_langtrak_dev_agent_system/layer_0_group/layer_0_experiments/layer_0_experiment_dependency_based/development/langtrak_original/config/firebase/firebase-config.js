// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics, isSupported } from "firebase/analytics";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCXoBKM6UQx5wCvBYQ_KvhCPmjcNyis9XE",
  authDomain: "lang-trak-dev.firebaseapp.com",
  projectId: "lang-trak-dev",
  storageBucket: "lang-trak-dev.firebasestorage.app",
  messagingSenderId: "894561101654",
  appId: "1:894561101654:web:fc234c159fd669749d98f7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Analytics only in supported environments (browser)
let analytics = null;
if (typeof window !== 'undefined') {
  isSupported().then((supported) => {
    if (supported) {
      analytics = getAnalytics(app);
    }
  });
}

export { app, analytics };
