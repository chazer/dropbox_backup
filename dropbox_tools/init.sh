
CONFIG_FILE=

while [[ "$1" == --* ]]; do
    PARAM="$1"; shift
    case "$PARAM" in
        --config=*)
            CONFIG_FILE="${PARAM//--config=}"
            ;;
        --config)
            CONFIG_FILE="$1"; shift
            ;;
    esac
done


if [ -f "$CONFIG_FILE" ]; then
    echo "load config form file $CONFIG_FILE" >&2
    source "$CONFIG_FILE"
fi


