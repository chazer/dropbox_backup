# [WIP] Dropbox backup tool

    Lightweight solution for storing backups in Dropbox, with encryption support

## Usage

### Check App

```
./dropbox_tools/dropbox_check_app --config=config.cfg
```

### Upload file

```
./dropbox_tools/dropbox_upload --config=config.cfg ./file.dat "/Backups/example.bin"
```

### Show folder content

```
./dropbox_tools/dropbox_folder_list --config=config.cfg "/Backups"
```

## How to get the Dropdox API Token

1. Create app

- Go to https://www.dropbox.com/developers/apps/create

- Choose "App folder" type and enter unique app name

2. Go to the app settings page

(you can found your apps on page https://www.dropbox.com/developers/apps)

- Dissallow implicit grants, Push "Generate Token" button

- Copy app user, app password and token

3. Make settings file

(see example.cfg as example)


## How to connect app to specific folder

Just move or rename app folder in Dropbox


