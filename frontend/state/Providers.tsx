'use client';
import { Provider } from "react-redux";
import { store } from "@/state/store";
import { ReactNode } from "react";
import { EnhancedStore } from "@reduxjs/toolkit";

export function Providers(props: { children: ReactNode, store: EnhancedStore}) {
  return <Provider store={store}>{props.children}</Provider>;
}
