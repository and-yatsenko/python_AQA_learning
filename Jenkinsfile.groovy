branchName  = "${branch_name}"
branchName  = "${test_suite}"

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/and-yatsenko/python_AQA_learning.git']])
            }
        }
        stage('Build') {
            steps {
                 // Создание виртуальной среды и установка пакетов
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Запуск автотестов (например, pytest)
                sh '. venv/bin/activate && pytest -s -v -m "${test_suite}" --alluredir allure-results'
            }
        }
        stage('Reports') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
