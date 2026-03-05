// resource_id: "1b433f20-2752-4459-b6a4-e06d6594e275"
// resource_type: "document"
// resource_name: "firestore-admin-client"
import fs from 'node:fs/promises';
import path from 'node:path';

let adminApp = null;
let firestoreInstance = null;

const SERVICE_ACCOUNT_PATH_ENV = 'FIREBASE_SERVICE_ACCOUNT_PATH';
const SERVICE_ACCOUNT_JSON_ENV = 'FIREBASE_ADMIN_CREDENTIALS';
const SERVICE_ACCOUNT_PROJECT_ENV = 'FIREBASE_ADMIN_PROJECT_ID';

async function loadServiceAccountConfig() {
  const inline = process.env[SERVICE_ACCOUNT_JSON_ENV];
  if (inline) {
    try {
      return JSON.parse(inline);
    } catch (error) {
      throw new Error(`FIREBASE_ADMIN_CREDENTIALS is not valid JSON: ${error.message}`);
    }
  }

  const configuredPath = process.env[SERVICE_ACCOUNT_PATH_ENV];
  if (configuredPath) {
    const resolved = path.resolve(configuredPath);
    const contents = await fs.readFile(resolved, 'utf-8');
    return JSON.parse(contents);
  }

  return null;
}

async function ensureAdminApp() {
  if (firestoreInstance) return firestoreInstance;

  const serviceAccount = await loadServiceAccountConfig();
  if (!serviceAccount) {
    return null;
  }

  const { cert, initializeApp, getApps, getApp } = await import('firebase-admin/app');
  const { getFirestore } = await import('firebase-admin/firestore');

  const apps = getApps();
  if (apps.length) {
    adminApp = getApp();
  } else {
    const projectId =
      serviceAccount.project_id ||
      process.env[SERVICE_ACCOUNT_PROJECT_ENV] ||
      undefined;

    adminApp = initializeApp({
      credential: cert(serviceAccount),
      projectId,
    });
  }

  firestoreInstance = getFirestore(adminApp);
  return firestoreInstance;
}

export async function getAdminFirestore() {
  return ensureAdminApp();
}
