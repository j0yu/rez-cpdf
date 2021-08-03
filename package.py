name = "cpdf"

__version__ = "2.4"
version = __version__ + "+local.1.0.0"

variants = [["platform-linux", "arch-x86_64"]]

relocatable = True

build_command = r"""
set -euf -o pipefail

case "$REZ_BUILD_VARIANT_INDEX" in
    0) VARIANT=Linux-Intel-64bit;;
    *)
        echo Not implemented
        exit 1
        ;;
esac

URL=https://github.com/coherentgraphics/cpdf-binaries/archive/refs/tags
URL+="/v{version}.tar.gz"
CURL_FLAGS=("-L")
[ -t 1 ] && CURL_FLAGS+=("-#") || CURL_FLAGS+=("-sS")

if [ $REZ_BUILD_INSTALL -eq 1 ]
then
    curl "{CURL_FLAGS}" "$URL" | tar -xz --strip-components=2 \
        -C "$REZ_BUILD_INSTALL_PATH" "cpdf-binaries-{version}"/"$VARIANT"/cpdf
fi
""".format(
    version=__version__,
    CURL_FLAGS="${{CURL_FLAGS[@]}}",
)


def commands():
    env.PATH.append("{root}")
