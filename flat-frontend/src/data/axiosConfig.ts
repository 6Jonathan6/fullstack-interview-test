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

interface Stats {
  deletions: number;
  file_name: string;
  insertions: number;
  lines: number;
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
  files_stats: Stats[];
  total_stats: {
    deletions: number;
    files: number;
    insertions: number;
    lines: number;
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

export function getCommitDetail(sha: string): AxiosPromise<Commit> {
  return api({
    url: `/commit/${sha}/`,
  });
}
