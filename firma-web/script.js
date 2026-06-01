const nombreInput = document.getElementById("nombreInput");
const cargoInput = document.getElementById("cargoInput");
const telefonoInput = document.getElementById("telefonoInput");
const nombreOutput = document.getElementById("nombre");
const cargoOutput = document.getElementById("cargo");
const telefonoOutput = document.getElementById("telefono");
const exportarBtn = document.getElementById("exportarBtn");
const firma = document.getElementById("firma");
const TELEFONO_FIJO = "+51 938 372 216";

function actualizarTexto(input, output, transformador) {
	input.addEventListener("input", (event) => {
		const valor = event.target.value;
		output.innerText = transformador ? transformador(valor) : valor;
	});
}

function actualizarTelefono() {
	const telefonoIngresado = telefonoInput.value.trim();
	telefonoOutput.innerText = telefonoIngresado
		? `${telefonoIngresado} / ${TELEFONO_FIJO}`
		: TELEFONO_FIJO;
}

async function exportar() {
	const imagenes = Array.from(firma.querySelectorAll("img"));
	const logo = firma.querySelector(".logo-container img");
	await Promise.all(
		imagenes.map(async (imagen) => {
			if (imagen.complete) {
				if (typeof imagen.decode === "function") {
					await imagen.decode().catch(() => {});
				}
				return;
			}

			await new Promise((resolve) => {
				imagen.addEventListener("load", resolve, { once: true });
				imagen.addEventListener("error", resolve, { once: true });
			});
		})
	);

	const firmaRect = firma.getBoundingClientRect();
	let recorteIzquierdo = 0;
	if (logo) {
		const logoRect = logo.getBoundingClientRect();
		const margenIzquierdo = 8;
		recorteIzquierdo = Math.max(0, Math.round(logoRect.left - firmaRect.left - margenIzquierdo));
	}

	const anchoExportacion = Math.max(1, Math.round(firmaRect.width - recorteIzquierdo));
	const altoExportacion = Math.max(1, Math.round(firmaRect.height));

	const canvasFinal = await html2canvas(firma, {
		backgroundColor: null,
		scale: 2,
		useCORS: true,
		allowTaint: false,
		x: recorteIzquierdo,
		y: 0,
		width: anchoExportacion,
		height: altoExportacion,
		windowWidth: Math.round(firmaRect.width),
		windowHeight: Math.round(firmaRect.height)
	});

	const link = document.createElement("a");
	link.download = "firma_gya.png";
	link.href = canvasFinal.toDataURL("image/png");
	link.click();
}

actualizarTexto(nombreInput, nombreOutput, (valor) => valor.toUpperCase());
actualizarTexto(cargoInput, cargoOutput);
telefonoInput.addEventListener("input", actualizarTelefono);
actualizarTelefono();
exportarBtn.addEventListener("click", exportar);
