pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "sudo docker-compose build"
            }
        }
        stage('Push'){
            steps {
                sh "sudo docker tag build_object_manipulation tibialzib/webservice:object_manipulation"
                sh "sudo docker tag build_colour_api tibialzib/webservice:colour_api"
                sh "sudo docker tag build_attributes_api tibialzib/webservice:attributes_api"
                sh "sudo docker tag build_front-end tibialzib/webservice:front-end"
                sh "sudo docker push tibialzib/webservice"
            }
        }
    }

}