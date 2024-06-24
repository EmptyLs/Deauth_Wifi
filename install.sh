#!/bin/bash

# Функция для проверки и установки пакетов с использованием apt
install_with_apt() {
    sudo apt update
    sudo apt install -y "$1"
}

# Функция для проверки и установки пакетов с использованием pacman
install_with_pacman() {
    sudo pacman -S --noconfirm "$1"
}

# Функция для проверки и установки пакетов с использованием yum
install_with_yum() {
    sudo yum install -y "$1"
}

# Функция для проверки и установки пакетов с использованием dnf
install_with_dnf() {
    sudo dnf install -y "$1"
}

# Функция для проверки и установки пакетов с использованием zypper
install_with_zypper() {
    sudo zypper install -y "$1"
}

# Проверка, существует ли команда
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Определение пакетного менеджера и установка пакетов
install_packages() {
    packages=("aircrack-ng" "gnome-terminal")

    if command_exists apt; then
        echo "Использование пакетного менеджера apt"
        for pkg in "${packages[@]}"; do
            if ! command_exists "$pkg"; then
                echo "Установка $pkg..."
                install_with_apt "$pkg"
            else
                echo "$pkg уже установлен"
            fi
        done
    elif command_exists pacman; then
        echo "Использование пакетного менеджера pacman"
        for pkg in "${packages[@]}"; do
            if ! command_exists "$pkg"; then
                echo "Установка $pkg..."
                install_with_pacman "$pkg"
            else
                echo "$pkg уже установлен"
            fi
        done
    elif command_exists yum; then
        echo "Использование пакетного менеджера yum"
        for pkg in "${packages[@]}"; do
            if ! command_exists "$pkg"; then
                echo "Установка $pkg..."
                install_with_yum "$pkg"
            else
                echo "$pkg уже установлен"
            fi
        done
    elif command_exists dnf; then
        echo "Использование пакетного менеджера dnf"
        for pkg in "${packages[@]}"; do
            if ! command_exists "$pkg"; then
                echo "Установка $pkg..."
                install_with_dnf "$pkg"
            else
                echo "$pkg уже установлен"
            fi
        done
    elif command_exists zypper; then
        echo "Использование пакетного менеджера zypper"
        for pkg in "${packages[@]}"; do
            if ! command_exists "$pkg"; then
                echo "Установка $pkg..."
                install_with_zypper "$pkg"
            else
                echo "$pkg уже установлен"
            fi
        done
    else
        echo "Ошибка: Поддерживаемый пакетный менеджер не найден. Установите aircrack-ng и gnome-terminal вручную."
        exit 1
    fi
}

# Запуск функции установки пакетов
install_packages

# Остальная часть install скрипта
echo "Выполнение других шагов установки..."
# Существующие шаги установки здесь

echo "Устонавливаем программу. Пожалуйста подождите, это может занять некоторое времья!"
cp -r install/wifi_deauth /usr/sbin/
chmod 777 /usr/sbin/wifi_deauth

pip install colorama --break-system-packages 

mkdir /prog 
mkdir /prog/Wifi_deauth/
cp -r install/setup.py /prog/Wifi_deauth/

echo "Установка была завершена для запуска программы пропишите команду wifi_deauth"
