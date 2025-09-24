pipeline {
    agent any

    stages {
        stage('Check Git') {
            steps {
                sh 'git --version'
                sh 'which git'
            }
        }
    }
}
