pipeline {
    /* Let the job picker override the agent */
    agent { label "${params.AGENT_LABEL ?: 'raspberrypi-gw'}" }

    parameters {
        string(name: 'AGENT_LABEL', defaultValue: 'raspberrypi-gw', description: 'Agent label to run this pipeline')
        string(name: 'SOURCE_DIR', defaultValue: '/tmp/source', description: 'Source directory')
        string(name: 'DESTINATION_DIR', defaultValue: '/tmp/target', description: 'Destination directory')
    }

    stages {
        stage('Starting Job') {
            steps {
                echo "Starting job: ${env.JOB_NAME}"
                echo "Running on agent: ${params.AGENT_LABEL}"
                echo "Source Directory: ${params.SOURCE_DIR}"
                echo "Destination Directory: ${params.DESTINATION_DIR}"
                echo "Workspace: ${env.WORKSPACE}"
            }
        }

        stage('Clean Workspace') {
            when { expression { return env.JOB_NAME?.endsWith('_check') } }
            steps {
                cleanWs()
            }
        }

        stage('Initial Checks') {
            when { expression { return env.JOB_NAME?.endsWith('_check') } }
            steps {
                echo 'Starting initial checks...'
                sh '''
                  git --version || true
                  which git || true
                  python3 --version || true
                  which python3 || true
                  ls -lsa
                  df -h
                  pip3 --version || true
                '''
            }
        }

        stage('Prepare Environment') {
            when { expression { return env.JOB_NAME?.endsWith('_prepare') } }
            steps {
                sh '''
                  echo "############################ Preparing Workspace ############################"
                  if [ ! -d "venv" ]; then
                      python3 -m venv venv
                  fi
                  # Prime pip in the venv
                  . venv/bin/activate
                  python -m pip install --upgrade pip
                '''
            }
        }

        stage('Starting Processes') {
            when { expression { return env.JOB_NAME?.endsWith('_run') } }
            steps {
                sh 'echo "############################ Starting Processes ############################"'
                // Prefer PATH prepend so we can just call `python`/`pip`
                withEnv(["PATH=${env.WORKSPACE}/venv/bin:${env.PATH}"]) {
                    sh '''
                      if [ ! -d "venv" ]; then
                          python3 -m venv venv
                      fi
                      python -m pip install --upgrade pip
                      if [ -f requirements.txt ]; then
                          python -m pip install -r requirements.txt
                      fi
                      python initializer.py
                    '''
                }
                echo 'Processes started successfully.'
            }
        }
    }
}
