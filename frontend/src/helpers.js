import { error, log, URL } from "./globals";

export const jsonWithStatus = r =>
  new Promise((resolve, reject) => {
    r.json()
      .then(data => {
        resolve({ ...data, status: r.status, ok: r.ok });
      })
      .catch(err => reject(err));
  });

export const GET = url =>
  fetch(url, {
    method: "GET",
    headers: {
      Accept: "application/json"
    },
    credentials: "include"
  })
    .then(res => jsonWithStatus(res))
    .catch(err => error(err));

export const POST = (url, body) =>
  fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    credentials: "include",
    body: JSON.stringify(body)
  })
    .then(res => jsonWithStatus(res))
    .catch(err => error(err));

export const checkAdmin = isadmin => {
  GET(`${URL}/user/isadmin`).then(res => {
    if (res.ok) {
      isadmin(true);
    } else if (res.status == 401) {
      isadmin(false);
    } else {
      log(res);
    }
  });
};
