﻿using System.Net.Http;
using System.Threading.Tasks;

namespace Fiap.Api.CriarContato.Services { 
    public class ContatoService : IContatoService
    {
        private readonly HttpClient _httpClient;
        private readonly string _consultarServiceUrl;

        public ContatoService(HttpClient httpClient)
        {
            _httpClient = httpClient;
            _consultarServiceUrl = Environment.GetEnvironmentVariable("ConsultarServiceUrl")
                                ?? throw new InvalidOperationException("Environment variable 'ConsultarServiceUrl' is not set.");
        }

        public async Task<HttpResponseMessage> ValidarContatoAsync(string ddd, string telefone, string email)
        {
            var requestUri = $"{_consultarServiceUrl}/ValidarContato?ddd={ddd}&telefone={telefone}&email={email}";
            return await _httpClient.GetAsync(requestUri);
        }
    }
}