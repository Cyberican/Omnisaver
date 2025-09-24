pipeline {
    agent { label "${AGENT_LABEL}" }

    parameters {
        string(name: 'AGENT_LABEL', defaultValue: 'raspberrypi-gw', description: 'Agent label to run this pipeline')
    }

    stages {
        stage('Initial Checks') {
            steps {
                echo 'Starting initial checks...'
                echo "Running on agent: ${AGENT_LABEL}..."
            }
        }
        stage('Check Git') {
            steps {
                sh 'git --version'
                sh 'which git'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
                sh 'which python3'
            }
        }

        stage('Check Filesystem') {
            steps {
                sh 'ls -lsa'
            }
        }

    }
}
