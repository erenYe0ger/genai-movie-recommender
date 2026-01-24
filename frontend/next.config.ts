import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    optimizeCss: false, // turn off LightningCSS
  },
};

export default nextConfig;
