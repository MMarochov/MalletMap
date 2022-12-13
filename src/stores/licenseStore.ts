import { writable } from "svelte/store";

const currentLicenseTerms = sessionStorage.licenseTermsAccepted
  ? JSON.parse(sessionStorage.licenseTermsAccepted)
  : false;
export const licenseTermsAccepted = writable(currentLicenseTerms);

licenseTermsAccepted.subscribe((value: boolean) => {
  sessionStorage.licenseTermsAccepted = JSON.stringify(value);
});
