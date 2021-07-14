pipeline{
        agent any
        stages{
            stage('Build Image'){
                steps{
                    sh "sudo docker-compose build"
                    }
                }
        
            stage('Tag & Push front-end'){
                steps{
                    sh "sudo docker tag build_front-end tibialzib/front-end:latest"
                    sh "sudo docker push tibialzib/front-end:latest"
                        }
                    }
            stage('Tag & Push object_maniputlation'){
                steps{
                    sh "sudo docker tag build_object_maniputlation tibialzib/object_maniputlation:latest"
                    sh "sudo docker push tibialzib/object_maniputlation:latest"
                        }
                    }
            stage('Tag & Push colour_api'){
                steps{
                    sh "sudo docker tag build_colour_api tibialzib/colour_api:latest"
                    sh "sudo docker push tibialzib/colour_api:latest"
                        }
                    }
            stage('Tag & Push attributes_api'){
                steps{
                    sh "sudo docker tag build_attributes_api tibialzib/attributes_api:latest"
                    sh "sudo docker push tibialzib/attributes_api:latest"
                        }
                    }
            stage('Deploy App'){
                steps{
                    sh "sudo docker-compose pull && docker-compose up -d"
                }
            }
        }
}