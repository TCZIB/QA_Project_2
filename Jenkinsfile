pipeline {
    agent any
    stages {
        stage ('Clean Machine') {
            steps{
                sh "sudo docker image prune -f"
            }
        }
        stage('Build') {
            steps {
                sh "sudo docker-compose build -t tibialzib/webservice"
            }
        }
        stage('Push'){
            steps {
                sh "sudo docker push tibialzib/webservice"
            }
        }
    }

}