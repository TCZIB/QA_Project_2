pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
                    sh "sudo docker-compose build"
                    }
                }
        
            stage('Tag & Push Image'){
                steps{
                    sh "sudo docker tag build_front-end tibialzib/front-end:latest"
                        }
                    }
            stage('Deploy App'){
                steps{
                    sh "docker-compose pull && docker-compose up -d"
                }
            }
        }
}