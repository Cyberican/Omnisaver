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
        stage('Check System Info') {
            steps {
                sh 'git --version'
                sh 'which git'
                sh 'python3 --version'
                sh 'which python3'
                sh 'ls -lsa'
                sh 'df -h'
            }
        }
        stage('Starting Processes') {
            steps {
                sh '''
                    echo "Starting necessary processes..."
                    # Add commands to start your processes here
                '''
                sh 'python initiate_process.py &'
                echo 'Processes started successfully.'
            }
        }
    }
}
