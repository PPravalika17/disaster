pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "ppravalika/disaster-app:latest"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker image"
                bat "docker build -t disaster-app:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging in to Docker Hub"
                bat 'docker login -u ppravalika -p Pravalika1709'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Tagging and pushing Docker image"
                bat "docker tag disaster-app:v1 ppravalika/disaster-app:latest"
                bat "docker push ppravalika/disaster-app:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
               bat 'kubectl set image deployment/disaster-app disaster-app=ppravalika/disaster-app:latest'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed. Please check the logs'
        }
    }
}
