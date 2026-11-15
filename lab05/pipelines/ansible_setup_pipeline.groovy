
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

        stage('Configure Test Server') {
            steps {
                dir('lab05/ansible') {
                    sh '''
                        ANSIBLE_HOST_KEY_CHECKING=False \
                        ansible-playbook \
                        -i hosts.ini \
                        setup_test_server.yml
                    '''
                }
            }
        }
    }
}
