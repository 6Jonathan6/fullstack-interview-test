import axios from "axios";
import { AxiosPromise } from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_APP_API_URL as string,
});

export function getBranches(): AxiosPromise<string[]> {
  return api({
    url: "/branches/",
    method: "get",
  });
}

export interface Commit {
  id: string;
  datetime: string;
  message: string;
  short_sha: string;
  author: {
    name: string;
    email: string;
  };
}
export function getBranchDetail(branchName: string): AxiosPromise<Commit[]> {
  return api({
    url: `/branches/`,
    params: {
      pk: branchName,
    },
    method: "get",
  });
}
