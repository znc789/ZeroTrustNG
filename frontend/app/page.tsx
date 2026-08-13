'use client';

import { useEffect, useMemo, useState } from 'react';

type DashboardData = {
  live_users: number;
  connected_devices: number;
  threats_detected: number;
  risk_score: number;
  alerts: Array<{ id: string; severity: string; title: string; source: string }>;
  widgets: { users: number; devices: number; network: string; mfa: number };
  timeline: Array<{ name: string; value: number }>;
  heatmap: Array<{ region: string; risk: number }>;
  posture: Array<[string, number]>;
  generated_at: string;
};

const defaultData: DashboardData = {
  live_users: 0,
  connected_devices: 0,
  threats_detected: 0,
  risk_score: 0,
  alerts: [],
  widgets: { users: 0, devices: 0, network: 'stable', mfa: 0 },
  timeline: [],
  heatmap: [],
  posture: [],
  generated_at: '',
};

const API_ENDPOINT = '/api/dashboard/overview';

export default function HomePage() {
  const [data, setData] = useState<DashboardData>(defaultData);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;

    const fetchDashboard = async () => {
      try {
        const response = await fetch(API_ENDPOINT, { cache: 'no-store' });
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }

        const result = await response.json();
        if (active) {
          setData(result);
          setError(null);
        }
      } catch (err) {
        if (active) {
          setError(err instanceof Error ? err.message : 'Failed to load dashboard');
        }
      } finally {
        if (active) setLoading(false);
      }
    };

    fetchDashboard();
    return () => {
      active = false;
    };
  }, []);

  const metricCards = useMemo(
    () => [
      { label: 'Live users', value: String(data.live_users), delta: '+12%' },
      { label: 'Connected devices', value: String(data.connected_devices), delta: '+8%' },
      { label: 'Active threats', value: String(data.threats_detected), delta: '-6%' },
      { label: 'Risk score', value: `${data.risk_score.toFixed(1)}`, delta: '+2.1%' },
    ],
    [data]
  );

  if (loading) {
    return <main className="min-h-screen p-6 md:p-10 grid-bg"><div className="mx-auto max-w-7xl panel rounded-2xl p-8 text-slate-200">Loading live zero-trust telemetry...</div></main>;
  }

  if (error) {
    return (
      <main className="min-h-screen p-6 md:p-10 grid-bg">
        <div className="mx-auto max-w-3xl panel rounded-2xl p-8 text-slate-200">
          <h1 className="text-xl font-semibold text-white">Runtime dashboard unavailable</h1>
          <p className="mt-3 text-slate-300">{error}</p>
          <p className="mt-3 text-sm text-cyan-300">The frontend could not reach the live security data source from this preview environment.</p>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen p-6 md:p-10 grid-bg">
      <div className="mx-auto max-w-7xl space-y-6">
        <header className="panel flex items-center justify-between rounded-2xl px-6 py-4">
          <div>
            <p className="text-xs uppercase tracking-[0.3em] text-cyan-300/80">Zero Trust Network Guardian</p>
            <h1 className="mt-2 text-2xl font-semibold text-white">AI-Powered Adaptive Security Operations</h1>
          </div>
          <div className="flex items-center gap-3">
            <div className="rounded-full border border-emerald-400/40 bg-emerald-500/10 px-3 py-1 text-xs text-emerald-300">
              Security posture: Strong
            </div>
            <button className="rounded-xl bg-cyan-500 px-4 py-2 text-sm font-medium text-slate-950 shadow-glow transition hover:bg-cyan-400">
              Run response playbook
            </button>
          </div>
        </header>

        <div className="flex justify-end text-xs text-slate-400">
          Updated: {new Date(data.generated_at || Date.now()).toLocaleTimeString()}
        </div>

        <section className="grid gap-4 md:grid-cols-4">
          {metricCards.map((metric) => (
            <div key={metric.label} className="metric-box">
              <div className="text-sm text-slate-300">{metric.label}</div>
              <div className="mt-4 flex items-end justify-between">
                <div className="text-3xl font-bold text-white">{metric.value}</div>
                <div className="text-xs text-emerald-400">{metric.delta}</div>
              </div>
            </div>
          ))}
        </section>

        <section className="grid gap-6 xl:grid-cols-[1.7fr_1fr]">
          <div className="panel rounded-2xl p-5">
            <div className="mb-4 flex items-center justify-between">
              <h2 className="text-lg font-semibold text-white">Threat timeline</h2>
              <span className="text-xs uppercase tracking-[0.25em] text-cyan-300">Live</span>
            </div>
            <div className="flex h-52 items-end gap-3">
              {data.timeline.map((bar) => (
                <div key={bar.name} className="flex flex-1 flex-col items-center gap-2">
                  <div
                    className="w-full rounded-t-xl bg-gradient-to-t from-cyan-500 via-sky-500 to-cyan-300"
                    style={{ height: `${bar.value * 2.4}px` }}
                  />
                  <span className="text-xs text-slate-400">{bar.name}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="panel rounded-2xl p-5">
            <h2 className="text-lg font-semibold text-white">Risk heatmap</h2>
            <div className="mt-5 space-y-4">
              {data.heatmap.map((item) => (
                <div key={item.region}>
                  <div className="mb-1 flex justify-between text-sm text-slate-300">
                    <span>{item.region}</span>
                    <span>{item.risk}</span>
                  </div>
                  <div className="h-2 rounded-full bg-slate-800">
                    <div
                      className="h-2 rounded-full bg-gradient-to-r from-emerald-400 via-amber-400 to-rose-500"
                      style={{ width: `${item.risk}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="grid gap-6 xl:grid-cols-[1.5fr_1fr]">
          <div className="panel rounded-2xl p-5">
            <h2 className="text-lg font-semibold text-white">Top threats</h2>
            <div className="mt-4 overflow-hidden rounded-xl border border-white/10">
              <table className="w-full text-left text-sm">
                <thead className="bg-slate-900/80 text-slate-300">
                  <tr>
                    <th className="p-3">Threat</th>
                    <th className="p-3">Severity</th>
                    <th className="p-3">Source</th>
                    <th className="p-3">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {data.alerts.map((row) => (
                    <tr key={row.id} className="border-t border-white/10">
                      <td className="p-3 text-slate-100">{row.title}</td>
                      <td className="p-3">
                        <span className={`rounded-full px-2 py-1 text-xs ${row.severity === 'critical' ? 'bg-rose-500/20 text-rose-300' : row.severity === 'high' ? 'bg-amber-500/20 text-amber-300' : 'bg-cyan-500/20 text-cyan-300'}`}>
                          {row.severity}
                        </span>
                      </td>
                      <td className="p-3 text-slate-300">{row.source}</td>
                      <td className="p-3 text-emerald-300">Active</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div className="panel rounded-2xl p-5">
            <h2 className="text-lg font-semibold text-white">Zero Trust posture</h2>
            <div className="mt-6 space-y-5">
              {data.posture.map(([label, percent]) => (
                <div key={label}>
                  <div className="mb-2 flex justify-between text-sm text-slate-300">
                    <span>{label}</span>
                    <span>{percent}%</span>
                  </div>
                  <div className="h-2 rounded-full bg-slate-800">
                    <div
                      className="h-2 rounded-full bg-gradient-to-r from-cyan-500 to-emerald-400"
                      style={{ width: `${percent}%` }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
