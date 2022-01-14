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

export const PULL_REQUEST_STATUS_OPEN = "OP";
export const PULL_REQUEST_STATUS_CLOSED = "CL";
export const PULL_REQUEST_STATUS_MERGED = "MR";
export const PULL_REQUEST_STATUSES = [
  PULL_REQUEST_STATUS_OPEN,
  PULL_REQUEST_STATUS_CLOSED,
  PULL_REQUEST_STATUS_MERGED,
] as const;

export const PR_STATUS_LABELS = {
  [PULL_REQUEST_STATUS_OPEN]: "OPEN",
  [PULL_REQUEST_STATUS_CLOSED]: "CLOSED",
  [PULL_REQUEST_STATUS_MERGED]: "MERGED",
};
export type PR_STATUSES_UNION = typeof PULL_REQUEST_STATUSES[number];
export interface PullRequest {
  id: number;
  status: PR_STATUSES_UNION;
  base_branch_name: string;
  compare_branch_name: string;
  created_at: string;
  updated_at: string;
  merge_commit_message: string;
  pr_title: string;
  author: string;
}

export function getPullRequests(): AxiosPromise<PullRequest[]> {
  return api({
    url: "/pull-request/",
  });
}

interface CreatePrPayload {
  status: FormDataEntryValue | string;
  base_branch_name: FormDataEntryValue | string;
  compare_branch_name: FormDataEntryValue | string;
  merge_commit_message: FormDataEntryValue | string;
  pr_title: FormDataEntryValue | string;
  author: FormDataEntryValue | string;
}

export function createPullRequest(data: CreatePrPayload) {
  return api({
    url: "/pull-request/",
    method: "POST",
    data,
  });
}

export function updatePullRequest(
  id: number,
  status: PR_STATUSES_UNION
): AxiosPromise<PullRequest> {
  return api({
    url: `/pull-request/${id}/`,
    method: "patch",
    data: {
      status,
    },
  });
}
