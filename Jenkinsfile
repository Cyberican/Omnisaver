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
