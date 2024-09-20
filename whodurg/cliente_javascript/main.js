const umc_client_key = "umc_client_key";
const umc_license_key = "umc_license_key";

/**
 * Incluir en la cabecera las credenciales
 */
const myHeaders = new Headers();
myHeaders.append("umc-client-key", umc_client_key);
myHeaders.append("umc-license-key", umc_license_key);

const requestOptions = {
    method: "GET",
    headers: myHeaders,
    redirect: "follow"
};

/**
 * @param {string} parametros
 * IncludeAtc: true | false 
 * MedProdLevel: 1 | 2 | 3
 * IngredientTranslations = es-ES | en-US 
 */
const parametros = "MedProdLevel=2&IncludeAtc=true&IngredientTranslations=es-ES"

/**
 * Request
 */
fetch(`https://api.who-umc.org/whodrug/download/v2/regional-drugs?${parametros}`, requestOptions)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.error(error));