pipeline {
agent any


environment {
DOCKERHUB_CRED = credentials('dockerhub-creds') // create in Jenkins: username/password
DOCKERHUB_USER = DOCKERHUB_CRED_USR
DOCKERHUB_PASS = DOCKERHUB_CRED_PSW
IMAGE = "${DOCKERHUB_CRED_USR}/disaster-app"
TAG = "${env.GIT_COMMIT.substring(0,7)}"
KUBECONFIG_CREDENTIALS = credentials('kubeconfig') // store kubeconfig file in Jenkins credentials
}


stages {
stage('Checkout') {
steps {
checkout scm
}
}


stage('Build Image') {
steps {
sh 'docker --version || true'
sh 'docker build -t ${IMAGE}:${TAG} .'
}
}


stage('Login & Push Image') {
steps {
sh 'echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin'
sh 'docker push ${IMAGE}:${TAG}'
sh 'docker tag ${IMAGE}:${TAG} ${IMAGE}:latest'
sh 'docker push ${IMAGE}:latest'
}
}


stage('Deploy to Kubernetes') {
steps {
// write kubeconfig from credentials into a file
sh '''
echo "$KUBECONFIG_CREDENTIALS" > kubeconfig
export KUBECONFIG=$PWD/kubeconfig
kubectl set image deployment/disaster-app disaster-app=${IMAGE}:${TAG} --record || true
kubectl apply -f k8s/service.yaml || true
kubectl rollout status deployment/disaster-app --timeout=120s || true
'''
}
}
}


post {
always {
cleanWs()
}
}
}