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
                    sh "sudo docker tag build_object_manipulation tibialzib/object_manipulation:latest"
                    sh "sudo docker push tibialzib/object_manipulation:latest"
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
            stage('Copy Compose'){
                steps{
                    sh "sudo scp ./build/docker-compose.yaml jenkinsn@manager-18-04:docker-compose.yaml"
                    sh "sudo ssh jenkins@manager-18-04 docker stack deploy --compose-file docker-compose.yaml webservice"
                }
            }
        }
}