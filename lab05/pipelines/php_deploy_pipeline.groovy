
pipeline {
    agent {
        label 'ansible-agent'
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Deploy PHP Project') {
            steps {
                dir('lab05/ansible') {
                    sh '''
                        ANSIBLE_HOST_KEY_CHECKING=False \
                        ansible-playbook \
                        -i hosts.ini \
                        deploy_php.yml
                    '''
                }
            }
        }
    }
}
