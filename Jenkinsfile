pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Example') {
            steps {
                echo "${params.Greeting} World!"
            }
        }
        stage('Pre-Test') {
            steps {
                echo 'Pre-Testing..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
