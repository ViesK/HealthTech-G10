import { api } from "../lib/api";

export async function getUserData(token: string) {
  return api<{ users: any }>("/protected", {
    method: "GET",
    headers: { Authorization: `Bearer ${token}` },
  });
}
