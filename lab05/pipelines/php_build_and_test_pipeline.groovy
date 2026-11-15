
pipeline {
    agent {
        label 'php-agent'
    }

    stages {

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('lab05/php-project') {
                    sh 'composer install --no-interaction --prefer-dist'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                dir('lab05/php-project') {
                    sh 'mkdir -p reports'

                    catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE') {
                        sh 'vendor/bin/phpunit --log-junit reports/phpunit.xml tests'
                    }
                }
            }
        }

        stage('Report Test Results') {
            steps {
                junit 'lab05/php-project/reports/phpunit.xml'
            }
        }
    }

    post {
        always {
            junit testResults: 'lab05/php-project/reports/phpunit.xml',
                  allowEmptyResults: true
        }
    }
}
