pipeline {
    environment {
        registry = "sonikxsvg/ci_cd"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
   
    agent any
    
    stages {
       // branch: 'first_experiment', 
        stage('Cloning Git') {
            steps {
                git  'https://github.com/SonicX/MLOps_itogProject_'
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run bowerInstall'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy Image') {
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}

