pipeline {
    agent any

    environment {
        REGISTRY = "docker.io/yourusername"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Detect Changed Services') {
            steps {
                script {
                    def changedFiles = sh(script: "git diff --name-only origin/main", returnStdout: true).trim().split("\n")
                    def changedServices = changedFiles.findAll { it ==~ /.*-service\/.*/ }
                        .collect { it.split("/")[0] }
                        .unique()
                    
                    echo "Changed services: ${changedServices}"
                    env.CHANGED_SERVICES = changedServices.join(",")
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }


        stage('Build & Push Images') {
            steps {
                script {
                    env.CHANGED_SERVICES.split(",").each { service ->
                        dir(service) {
                            def image = "${REGISTRY}/${service}:latest"
                            sh "docker build -t ${image} ."
                            sh "docker push ${image}"
                        }
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    env.CHANGED_SERVICES.split(",").each { service ->
                        sh "kubectl apply -f k8s/${service}.yaml"
                    }
                }
            }
        }
    }
}
