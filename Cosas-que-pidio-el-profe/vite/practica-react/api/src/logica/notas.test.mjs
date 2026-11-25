import { describe, expect, it } from 'vitest';
import reglas from './notas.js';

describe('Aprobación', () => {
  it('aprueba exactamente 3.0', () => expect(reglas.aprobado(3)).toBe(true));
  it('reprueba por debajo del mínimo', () => expect(reglas.aprobado(2.9)).toBe(false));
  it('aprueba por encima del mínimo', () => expect(reglas.aprobado(4)).toBe(true));
});

describe('Registro y resumen', () => {
  it.each([0, 5])('acepta la nota extrema %s', nota => {
    expect(reglas.validarEstudiante({ nombre: 'Ana', nota })).toBeNull();
  });
  it.each([-1, 6, null, '3'])('rechaza la nota inválida %s', nota => {
    expect(reglas.validarEstudiante({ nombre: 'Ana', nota })).toMatch(/número/);
  });
  it('rechaza nombres en blanco', () => {
    expect(reglas.validarEstudiante({ nombre: ' ', nota: 4 })).toMatch(/nombre/);
  });
  it('distingue un grupo vacío de un promedio cero', () => {
    expect(reglas.resumen([])).toEqual({ total: 0, promedio: null, aprobados: 0 });
  });
  it('calcula el promedio y cuenta aprobados', () => {
    expect(reglas.resumen([{ nota: 5 }, { nota: 2 }])).toEqual({ total: 2, promedio: 3.5, aprobados: 1 });
  });
});
