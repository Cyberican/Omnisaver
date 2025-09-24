pipeline {
    agent { label 'raspberrypi-gw' }

    parameters {
        string(name: 'AGENT_LABEL', defaultValue: 'raspberrypi-gw', description: 'Agent label to run this pipeline')
        string(name: 'SOURCE_DIR', defaultValue: '/tmp/source', description: 'Source directory')
        string(name: 'DESTINATION_DIR', defaultValue: '/tmp/target', description: 'Destination directory')
    }

    stages {
        stage('Initial Checks') {
            steps {
                echo 'Starting initial checks...'
                echo "Running on agent: ${params.AGENT_LABEL}..."
                echo "Source Directory: ${params.SOURCE_DIR}"
                echo "Destination Directory: ${params.DESTINATION_DIR}"
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
                sh 'pip3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '############################ Installing Dependencies ############################'
                sh 'pip3 install upgrade pip -y'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Starting Processes') {
            steps {
                sh '############################ Starting Processes ############################'
                sh 'python3 initializer.py'
                echo 'Processes started successfully.'
            }
        }
    }
}
