pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
            steps {
                if (isUnix()){
                    sh "${pythHome}/bin/python"
                } else {
                    bat(/"${pythHome}")
                }
            }
        }
    }
}