pipeline {
    agent { label 'raspberrypi-gw' }

    parameters {
        string(name: 'AGENT_LABEL', defaultValue: 'raspberrypi-gw', description: 'Agent label to run this pipeline')
        string(name: 'SOURCE_DIR', defaultValue: '/tmp/source', description: 'Source directory')
        string(name: 'DESTINATION_DIR', defaultValue: '/tmp/target', description: 'Destination directory')
    }

    stages {
        stage('Starting Job') {
            steps {
               echo "Starting job: ${job.name}"
            }
        }

        // Run the checks stage
        if (job.name.endsWith('_check')) {
            stage('Clean Workspace') {
                steps {
                    cleanWs()
                }
            }
            stage('Initial Checks') {
                steps {
                    echo 'Starting initial checks...'
                    echo "Running on agent: ${params.AGENT_LABEL}..."
                    echo "Source Directory: ${params.SOURCE_DIR}"
                    echo "Destination Directory: ${params.DESTINATION_DIR}"
                    echo "My Current Workspace: $WORKSPACE"
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
        }

        // Prepare the environment
        if (job.name.endsWith('_prepare')) {
            stage('Prepare Environment') {
                steps {
                    sh '############################ Preparing Workspace ############################'
                    sh 'python3 -m venv venv'
                }
            }
        }

        // Run the initializer
        if (job.name.endsWith('_run')) {
            stage('Starting Processes') {
                steps {
                    sh '############################ Starting Processes ############################'
                    withEnv(["PATH=$WORKSPACE/venv/bin:$PATH"]) {
                        sh '''
                        pip3 install --upgrade pip
                        pip3 install -r requirements.txt
                        python3 initializer.py
                        '''
                    }
                    echo 'Processes started successfully.'
                }
            }
        }
    }
}
