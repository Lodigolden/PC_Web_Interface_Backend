SUMMARY = "A web interface backend for the personal computer"
LICENSE = "MIT"
LIC_FILES_CHKSUM = 

# Source files location.
SRC_URI = "file://src/main.py \
"
S = "${WORKDIR}"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 ${WORKDIR}/src/main.py ${D}${bindir}/pc-web-interface-backend
}

FILES:${PN} += "${bindir}/pc-web-interface-backend"
