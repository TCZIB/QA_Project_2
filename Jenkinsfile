pipeline{
    agent any
    stages{
        stage(' Testing ')
            steps{
                //
            }
        stage(' Install Docker and Init Swarm ')
            steps{
                sh "ansible-playbook -i inventory.yaml playbook.yaml"
            }
        stage(' Build App Images ')
            steps{
                sh "sudo docker-compose build"
            }
        stage(' Push Images To DockerHub')
            steps{
                sh " "
            }
    }
}

